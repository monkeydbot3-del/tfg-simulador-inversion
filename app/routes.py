import csv
import io
import json
import math
import random
import unicodedata
import uuid
from datetime import date, datetime, timedelta
from pathlib import Path

from flask import (
    Blueprint,
    Response,
    jsonify,
    redirect,
    render_template,
    request,
    send_from_directory,
    session,
    url_for,
)
import pandas as pd
import yfinance as yf
from yfinance.exceptions import YFRateLimitError

from .services.auth_service import get_user_by_id
from .models import ReadinessQuizResult
from .services.history_service import list_analysis_for_user, save_analysis_for_user


bp = Blueprint("main", __name__)

READINESS_PASS_SCORE = 7
READINESS_TOTAL_QUESTIONS = 10
READINESS_QUIZ_SESSION_KEY = "readiness_quiz_questions"
HORIZON_MAX_ASSETS = 5
HORIZON_DEFAULT_HORIZON_YEARS = 3
HORIZON_MAX_HORIZON_YEARS = 5
HORIZON_WARNING_KEY = "horizon_disclaimer_ack"
HORIZON_DISCLAIMER_TEXT = (
    "Esta simulación no predice el futuro. Se trata de una proyección experimental generada a partir de patrones históricos. "
    "En inversión, los resultados pasados no garantizan resultados futuros. Esta herramienta tiene finalidad educativa y demostrativa, "
    "no debe usarse para tomar decisiones financieras reales."
)
HORIZON_METHOD_DESCRIPTION = (
    "Este modo remezcla patrones de rentabilidad histórica para construir una trayectoria futura hipotética. "
    "No calcula lo que va a ocurrir, sino un escenario experimental posible dentro de una simulación educativa."
)
READINESS_QUIZ_QUESTIONS = [
    {
        "id": "risk_return",
        "prompt": "¿Qué suele ocurrir cuando una inversión ofrece potencial de rentabilidad más alto?",
        "options": [
            "Normalmente también implica más riesgo.",
            "Garantiza beneficios sin caídas.",
            "Siempre bate al benchmark.",
            "Reduce automáticamente la volatilidad.",
        ],
        "correctIndex": 0,
        "explanation": "Mayor rentabilidad esperada suele venir acompañada de mayor incertidumbre y oscilación.",
        "topic": "riesgo-rentabilidad",
    },
    {
        "id": "diversification",
        "prompt": "¿Cuál es el principal objetivo de diversificar una cartera?",
        "options": [
            "Reducir el impacto de un único activo o sector.",
            "Eliminar por completo el riesgo.",
            "Duplicar siempre la rentabilidad.",
            "Evitar comparar con un benchmark.",
        ],
        "correctIndex": 0,
        "explanation": "Diversificar ayuda a no depender demasiado de una sola posición, aunque no elimina todo el riesgo.",
        "topic": "diversificación",
    },
    {
        "id": "benchmark",
        "prompt": "En esta aplicación, ¿para qué sirve el benchmark?",
        "options": [
            "Para comparar el comportamiento de tu cartera frente a una referencia.",
            "Para fijar automáticamente el precio de compra.",
            "Para ocultar la volatilidad del portfolio.",
            "Para guardar sesiones en el historial.",
        ],
        "correctIndex": 0,
        "explanation": "El benchmark permite ver si tu cartera lo hace mejor, peor o parecido a una referencia de mercado.",
        "topic": "benchmark",
    },
    {
        "id": "volatility",
        "prompt": "¿Qué describe mejor la volatilidad?",
        "options": [
            "La intensidad con la que el valor de una inversión sube y baja en el tiempo.",
            "El capital inicial invertido.",
            "La rentabilidad acumulada garantizada.",
            "La cantidad de turnos del modo carrera.",
        ],
        "correctIndex": 0,
        "explanation": "La volatilidad mide la variabilidad de los precios o rendimientos, no si algo es bueno o malo por sí solo.",
        "topic": "volatilidad",
    },
    {
        "id": "dca",
        "prompt": "¿Qué representa DCA o inversión periódica en la app?",
        "options": [
            "Aportar cantidades periódicas para repartir el punto de entrada en el tiempo.",
            "Comprar solo cuando el benchmark cae.",
            "Una técnica para eliminar drawdowns.",
            "Un modo de exportar el informe final.",
        ],
        "correctIndex": 0,
        "explanation": "DCA reparte las compras en el tiempo y puede suavizar el riesgo de entrar todo en un solo punto.",
        "topic": "dca",
    },
    {
        "id": "drawdown",
        "prompt": "¿Qué indica un drawdown en el informe final?",
        "options": [
            "La caída desde un máximo previo hasta un mínimo posterior.",
            "La rentabilidad anual compuesta exacta.",
            "El número de operaciones realizadas.",
            "El peso del benchmark en la cartera.",
        ],
        "correctIndex": 0,
        "explanation": "El drawdown ayuda a entender cuánto llegó a retroceder una estrategia desde su mejor punto anterior.",
        "topic": "drawdown",
    },
    {
        "id": "simulation_vs_real",
        "prompt": "¿Qué diferencia clave existe entre esta app y una inversión real?",
        "options": [
            "La app simula escenarios con datos históricos y no ejecuta operaciones reales.",
            "La app garantiza resultados futuros.",
            "La app elimina los riesgos de mercado.",
            "La app obliga a comprar acciones reales al cerrar un turno.",
        ],
        "correctIndex": 0,
        "explanation": "La herramienta es educativa: compara escenarios y decisiones, pero no invierte dinero real.",
        "topic": "simulación",
    },
    {
        "id": "career_turns",
        "prompt": "¿Qué implica tomar decisiones por turnos en el Modo Carrera?",
        "options": [
            "Ajustar la cartera en distintos tramos históricos y observar cómo evoluciona.",
            "Repetir siempre la misma asignación sin contexto.",
            "Ignorar los eventos y el benchmark.",
            "Bloquear el historial del usuario.",
        ],
        "correctIndex": 0,
        "explanation": "El Modo Carrera divide el periodo en fases para que tomes decisiones y veas su impacto acumulado.",
        "topic": "modo-carrera",
    },
    {
        "id": "final_report",
        "prompt": "En el informe final, ¿qué comparan Portfolio, Benchmark y Tracking?",
        "options": [
            "El resultado de tu cartera, la referencia de mercado y la diferencia entre ambos.",
            "Tres formas distintas de guardar la sesión.",
            "El capital inicial, el capital final y el correo del usuario.",
            "La teoría, el historial y el login.",
        ],
        "correctIndex": 0,
        "explanation": "Portfolio resume tu estrategia, Benchmark la referencia y Tracking cómo te separas de ella.",
        "topic": "informe-final",
    },
    {
        "id": "auth_history",
        "prompt": "¿Qué ventaja principal tiene usar una cuenta autenticada frente al modo invitado?",
        "options": [
            "Conservar historial y progreso, incluido el acceso al Modo Carrera, entre sesiones.",
            "Eliminar automáticamente la volatilidad.",
            "Obtener una rentabilidad mejor en el informe.",
            "Acceder a precios futuros reales.",
        ],
        "correctIndex": 0,
        "explanation": "La autenticación permite persistir historial, sesiones de carrera y el aprobado del test entre accesos.",
        "topic": "usuarios-autenticados",
    },
]


# ----------------------
#   Vistas HTML
# ----------------------
@bp.get("/")
def home():
    if not _current_user_id() and not session.get("guest"):
        return redirect(url_for("auth.login_page"))
    current_user = get_user_by_id(_current_user_id()) if _current_user_id() else None
    return render_template("home.html", active="home", nav_mode="landing", current_user=current_user)


@bp.get("/inicio")
def inicio_alias():
    return render_template("inicio.html", active="inicio", nav_mode="practice")


@bp.get("/empresas")
def empresas_page():
    accept = request.accept_mimetypes
    wants_json = request.args.get("format") == "json" or (
        accept.best == "application/json"
        or accept["application/json"] >= accept["text/html"]
    )
    if wants_json and request.args.get("format") != "html":
        return listar_empresas()
    return render_template("empresas.html", active="empresas", nav_mode="practice")


@bp.get("/nuevo-analisis")
def analisis_page():
    return render_template("analisis.html", active="analisis", nav_mode="practice")


@bp.get("/historial")
def historial_page():
    if _is_guest_user():
        return redirect(url_for("main.home"))
    if not _current_user_id():
        return redirect(url_for("auth.login_page"))
    return render_template("historial.html", active="historial", nav_mode="practice")


def _current_user_id() -> int | None:
    raw = session.get("user_id")
    try:
        return int(raw) if raw is not None else None
    except (TypeError, ValueError):
        return None


def _is_guest_user() -> bool:
    return bool(session.get("guest")) and not bool(session.get("user_id"))


def _build_readiness_question_set() -> list[dict]:
    prepared = []
    for item in READINESS_QUIZ_QUESTIONS:
        options = []
        for index, label in enumerate(item["options"]):
            options.append(
                {
                    "id": f"{item['id']}:opt:{index}",
                    "label": label,
                    "correct": index == int(item["correctIndex"]),
                }
            )
        random.shuffle(options)
        prepared.append(
            {
                "id": item["id"],
                "prompt": item["prompt"],
                "options": options,
                "explanation": item["explanation"],
                "topic": item["topic"],
            }
        )
    random.shuffle(prepared)
    return prepared


def _get_or_create_readiness_question_set(force_new: bool = False) -> list[dict]:
    stored = session.get(READINESS_QUIZ_SESSION_KEY)
    if force_new or not stored:
        stored = _build_readiness_question_set()
        session[READINESS_QUIZ_SESSION_KEY] = stored
        session.modified = True
    return stored


def _clear_readiness_question_set() -> None:
    session.pop(READINESS_QUIZ_SESSION_KEY, None)
    session.modified = True


def _readiness_status_payload() -> dict:
    current_user_id = _current_user_id()
    if current_user_id:
        record = ReadinessQuizResult.select().where(ReadinessQuizResult.user == current_user_id).first()
        passed = bool(record.passed) if record else False
        return {
            "passed": passed,
            "score": record.score if record else 0,
            "total_questions": record.total_questions if record else READINESS_TOTAL_QUESTIONS,
            "pass_score": READINESS_PASS_SCORE,
            "storage": "server",
            "user_authenticated": True,
            "guest": False,
            "passed_at": record.passed_at.isoformat() + "Z" if record and record.passed_at else None,
        }

    guest_payload = session.get("readiness_guest") or {}
    passed = bool(guest_payload.get("passed"))
    return {
        "passed": passed,
        "score": int(guest_payload.get("score") or 0),
        "total_questions": int(guest_payload.get("total_questions") or READINESS_TOTAL_QUESTIONS),
        "pass_score": READINESS_PASS_SCORE,
        "storage": "session",
        "user_authenticated": False,
        "guest": _is_guest_user(),
        "passed_at": guest_payload.get("passed_at"),
    }


@bp.get("/aprende")
def aprende_page():
    return render_template(
        "aprende.html",
        active="aprende",
        nav_mode="practice",
        readiness_status=_readiness_status_payload(),
        readiness_pass_score=READINESS_PASS_SCORE,
        readiness_total_questions=READINESS_TOTAL_QUESTIONS,
    )


@bp.get("/manual")
def manual_page():
    return render_template("manual.html", active="manual", nav_mode="manual")


def _horizon_ack_key() -> str:
    user_id = _current_user_id()
    if user_id:
        return f"user:{user_id}"
    if _is_guest_user():
        return "guest"
    return "anon"


def _horizon_acknowledged() -> bool:
    payload = session.get(HORIZON_WARNING_KEY) or {}
    if not isinstance(payload, dict):
        return False
    return bool(payload.get(_horizon_ack_key()))


def _set_horizon_acknowledged() -> None:
    payload = session.get(HORIZON_WARNING_KEY) or {}
    if not isinstance(payload, dict):
        payload = {}
    payload[_horizon_ack_key()] = True
    session[HORIZON_WARNING_KEY] = payload
    session.modified = True


def _normalize_horizon_weights(assets: list[dict]) -> list[dict]:
    cleaned = []
    total_weight = 0.0
    for asset in assets:
        ticker = str(asset.get("ticker") or "").strip().upper()
        if not ticker:
            continue
        try:
            weight = float(asset.get("weight") or 0)
        except (TypeError, ValueError):
            weight = 0.0
        if weight < 0:
            weight = 0.0
        cleaned.append({"ticker": ticker, "weight": weight})
        total_weight += weight

    if not cleaned:
        return []

    if total_weight <= 0:
        even_weight = round(1 / len(cleaned), 6)
        return [{**asset, "weight": even_weight} for asset in cleaned]

    return [{**asset, "weight": asset["weight"] / total_weight} for asset in cleaned]


def _horizon_identity_payload() -> dict:
    return {
        "acknowledged": _horizon_acknowledged(),
        "disclaimer": HORIZON_DISCLAIMER_TEXT,
        "method_description": HORIZON_METHOD_DESCRIPTION,
        "max_assets": HORIZON_MAX_ASSETS,
        "default_horizon_years": HORIZON_DEFAULT_HORIZON_YEARS,
        "max_horizon_years": HORIZON_MAX_HORIZON_YEARS,
    }


@bp.get("/modo-horizonte")
def horizon_page():
    return render_template(
        "horizon.html",
        active="horizon",
        nav_mode="practice",
        horizon_config=_horizon_identity_payload(),
    )


@bp.post("/api/horizon/disclaimer/accept")
def horizon_accept_disclaimer_api():
    _set_horizon_acknowledged()
    return jsonify({"ok": True, **_horizon_identity_payload()})


@bp.get("/api/horizon/from-career/<session_id>")
def horizon_from_career_api(session_id: str):
    from .career import _resolve_session_for_request

    session_payload = _resolve_session_for_request(session_id)
    if not session_payload:
        return jsonify({"error": "No se pudo acceder a la sesión de carrera indicada."}), 404

    portfolio = session_payload.get("portfolio") or {}
    positions = portfolio.get("positions") or []
    assets = []
    for position in positions:
        ticker = str(position.get("ticker") or "").strip().upper()
        if not ticker or ticker == "CASH":
            continue
        try:
            weight = float(position.get("weight") or 0)
        except (TypeError, ValueError):
            weight = 0.0
        assets.append({"ticker": ticker, "weight": weight})

    normalized_assets = _normalize_horizon_weights(assets)[:HORIZON_MAX_ASSETS]
    final_value = portfolio.get("total_value") or portfolio.get("portfolio_value") or session_payload.get("capital") or 10000
    try:
        initial_value = float(final_value)
    except (TypeError, ValueError):
        initial_value = 10000.0

    return jsonify(
        {
            "source": "career",
            "session_id": session_id,
            "assets": normalized_assets,
            "initial_value": max(initial_value, 1000.0),
            "disclaimer": HORIZON_DISCLAIMER_TEXT,
            "method_description": HORIZON_METHOD_DESCRIPTION,
        }
    )


@bp.post("/api/horizon/simulate")
def horizon_simulate_api():
    payload = request.get_json(silent=True) or {}
    tickers_raw = payload.get("tickers")
    assets_raw = payload.get("assets")
    source = str(payload.get("source") or "manual").strip().lower() or "manual"
    session_id = str(payload.get("session_id") or "").strip()

    assets_input = []
    if isinstance(assets_raw, list) and assets_raw:
        assets_input = assets_raw
    elif isinstance(tickers_raw, list):
        assets_input = [{"ticker": item} for item in tickers_raw]

    assets = _normalize_horizon_weights(assets_input)
    if not assets:
        return jsonify({"error": "Debes seleccionar al menos un activo válido para generar el escenario experimental."}), 400
    if len(assets) > HORIZON_MAX_ASSETS:
        return jsonify({"error": f"El modo Horizonte admite como máximo {HORIZON_MAX_ASSETS} activos en esta versión."}), 400

    try:
        horizon_years = int(payload.get("horizon") or HORIZON_DEFAULT_HORIZON_YEARS)
    except (TypeError, ValueError):
        horizon_years = 0
    if horizon_years < 1 or horizon_years > HORIZON_MAX_HORIZON_YEARS:
        return jsonify({"error": f"Selecciona un horizonte válido entre 1 y {HORIZON_MAX_HORIZON_YEARS} años."}), 400

    try:
        initial_value = float(payload.get("initial_value") or 10000)
    except (TypeError, ValueError):
        initial_value = 10000.0
    if initial_value <= 0:
        return jsonify({"error": "El valor inicial debe ser mayor que cero."}), 400

    if source == "career" and session_id:
        from .career import _resolve_session_for_request

        if not _resolve_session_for_request(session_id):
            return jsonify({"error": "No puedes usar una sesión de carrera ajena o inexistente como origen."}), 404

    end_d = date.today()
    start_d = end_d - timedelta(days=365 * 8)
    warnings = []
    valid_assets = []
    monthly_returns = []
    provider_temporarily_limited = False

    for asset in assets:
        ticker = asset["ticker"]
        try:
            df = _download_history_df(ticker, start_d, end_d, include_actions=False)
            price_series = _extract_market_price_series(df, ticker)
            monthly = _compute_horizon_monthly_returns(df, ticker)
        except BacktestError as exc:
            if exc.status_code >= 500:
                provider_temporarily_limited = True
            warnings.append(str(exc))
            continue
        except HorizonSimulationError as exc:
            warnings.append(str(exc))
            continue
        except Exception:
            warnings.append(f"{ticker} se ha excluido porque no se pudo normalizar su histórico de mercado.")
            continue

        if price_series.empty or len(price_series) < 120:
            warnings.append(f"{ticker} se ha excluido porque no dispone de un historial útil para esta simulación experimental.")
            continue

        valid_assets.append({"ticker": ticker, "weight": asset["weight"], "series": price_series})
        monthly_returns.append(monthly.rename(ticker))

    if not valid_assets:
        status_code = 503 if provider_temporarily_limited else 400
        error_message = (
            "No se pudieron obtener datos del activo en este momento. La fuente de mercado ha limitado temporalmente las peticiones. Prueba de nuevo dentro de unos segundos o utiliza otro activo."
            if provider_temporarily_limited
            else "No hay datos históricos suficientes para construir el escenario experimental con los activos seleccionados."
        )
        return jsonify({"error": error_message, "warnings": warnings}), status_code

    total_valid_weight = sum(item["weight"] for item in valid_assets) or 1.0
    valid_assets = [{**item, "weight": item["weight"] / total_valid_weight} for item in valid_assets]

    hist_length = min(260, max(90, horizon_years * 52))
    hist_frames = []
    for item in valid_assets:
        series = item["series"].tail(hist_length)
        values = pd.to_numeric(series, errors="coerce").dropna()
        if values.empty:
            continue
        normalized = values / float(values.iloc[0]) * 100
        hist_frames.append(normalized.rename(item["ticker"]))
    hist_df = pd.concat(hist_frames, axis=1).dropna(how="all") if hist_frames else pd.DataFrame()
    if hist_df.empty:
        return jsonify({"error": "No se pudo construir la serie histórica base para el escenario experimental.", "warnings": warnings}), 400
    hist_df = hist_df.ffill().dropna(how="any")
    hist_weights = pd.Series({item["ticker"]: item["weight"] for item in valid_assets if item["ticker"] in hist_df.columns})
    hist_weights = hist_weights / hist_weights.sum()
    blended_hist = hist_df.mul(hist_weights, axis=1).sum(axis=1)

    monthly_df = pd.concat(monthly_returns, axis=1).dropna(how="all")
    monthly_df = monthly_df.ffill().dropna(how="any")
    if monthly_df.empty:
        return jsonify({"error": "No se pudieron combinar patrones mensuales suficientes para generar el escenario experimental.", "warnings": warnings}), 400

    weights = pd.Series({item["ticker"]: item["weight"] for item in valid_assets})
    available_cols = [col for col in monthly_df.columns if col in weights.index]
    monthly_df = monthly_df[available_cols]
    weights = weights[available_cols]
    weights = weights / weights.sum()
    blended_monthly = monthly_df.mul(weights, axis=1).sum(axis=1)
    if blended_monthly.empty:
        return jsonify({"error": "No hay patrones mensuales suficientes para proyectar el escenario experimental.", "warnings": warnings}), 400

    future_months = horizon_years * 12
    rng_seed = sum(sum(ord(ch) for ch in item["ticker"]) for item in valid_assets) + future_months + int(initial_value)
    rng = random.Random(rng_seed)
    sample_pool = blended_monthly.tolist()
    simulated_returns = [sample_pool[rng.randrange(len(sample_pool))] for _ in range(future_months)]

    future_dates = pd.date_range(start=date.today() + timedelta(days=30), periods=future_months, freq="ME")
    projected_base = [100.0]
    projected_value = [float(initial_value)]
    for ret in simulated_returns:
        projected_base.append(projected_base[-1] * (1 + float(ret)))
        projected_value.append(projected_value[-1] * (1 + float(ret)))

    historical_series = [[idx.isoformat(), round(float(value), 4)] for idx, value in blended_hist.items()]
    projected_series = [[future_dates[idx].date().isoformat(), round(float(projected_base[idx + 1]), 4)] for idx in range(future_months)]

    final_value = projected_value[-1]
    total_return = (final_value / initial_value) - 1 if initial_value else 0.0
    annualized = (final_value / initial_value) ** (1 / horizon_years) - 1 if initial_value and horizon_years > 0 else 0.0
    volatility = pd.Series(simulated_returns).std() * math.sqrt(12) if len(simulated_returns) > 1 else 0.0

    return jsonify(
        {
            "disclaimer": HORIZON_DISCLAIMER_TEXT,
            "historical_series": historical_series,
            "projected_series": projected_series,
            "metrics": {
                "initial_value": round(float(initial_value), 2),
                "projected_final_value": round(float(final_value), 2),
                "simulated_total_return": round(float(total_return), 6),
                "simulated_annualized_return": round(float(annualized), 6),
                "simulated_volatility": round(float(volatility), 6),
                "assets_used": [item["ticker"] for item in valid_assets],
                "horizon_years": horizon_years,
            },
            "warnings": warnings,
            "method_description": HORIZON_METHOD_DESCRIPTION,
            "source": source,
            "session_id": session_id or None,
            "assets": [{"ticker": item["ticker"], "weight": round(float(item["weight"]), 6)} for item in valid_assets],
        }
    )


@bp.get("/modo-carrera")
def career_page():
    readiness_status = _readiness_status_payload()
    return render_template(
        "career.html",
        active="career",
        nav_mode="career",
        readiness_status=readiness_status,
        readiness_gate_blocked=not readiness_status.get("passed"),
    )


@bp.get("/api/readiness/status")
def readiness_status_api():
    payload = _readiness_status_payload()
    payload["required_score"] = READINESS_PASS_SCORE
    payload["total_questions_default"] = READINESS_TOTAL_QUESTIONS
    return jsonify(payload)


@bp.get("/api/readiness/questions")
def readiness_questions_api():
    restart = request.args.get("restart") in {"1", "true", "yes"}
    questions = _get_or_create_readiness_question_set(force_new=restart)
    public_questions = []
    for index, item in enumerate(questions, start=1):
        public_questions.append(
            {
                "id": item["id"],
                "prompt": item["prompt"],
                "options": [{"id": option["id"], "label": option["label"]} for option in item["options"]],
                "explanation": item["explanation"],
                "topic": item["topic"],
                "step": index,
                "contextTitle": "Conceptos básicos" if index <= 5 else "Cómo leer la simulación",
                "contextHint": (
                    "Piensa en riesgo, diversificación, benchmark y horizonte temporal."
                    if index <= 5
                    else "Relaciona cada respuesta con las pantallas, métricas y decisiones de la app."
                ),
            }
        )
    return jsonify(
        {
            "questions": public_questions,
            "pass_score": READINESS_PASS_SCORE,
            "total_questions": len(public_questions),
        }
    )


@bp.post("/api/readiness/submit")
def readiness_submit_api():
    payload = request.get_json(silent=True) or {}
    answers = payload.get("answers") or []
    if not isinstance(answers, list):
        return jsonify({"error": "El formato de respuestas no es válido."}), 400

    question_set = _get_or_create_readiness_question_set()
    if len(answers) != len(question_set):
        return jsonify({"error": "Debes responder todas las preguntas del recorrido final."}), 400

    score = 0
    result_items = []
    question_map = {item["id"]: item for item in question_set}
    for answer in answers:
        if not isinstance(answer, dict):
            return jsonify({"error": "Cada respuesta debe indicar pregunta y opción."}), 400
        question_id = answer.get("questionId")
        option_id = answer.get("optionId")
        question = question_map.get(question_id)
        if not question:
            return jsonify({"error": "Se ha detectado una pregunta no válida en el intento."}), 400
        selected_option = next((option for option in question["options"] if option["id"] == option_id), None)
        correct_option = next((option for option in question["options"] if option["correct"]), None)
        is_correct = bool(selected_option and correct_option and selected_option["id"] == correct_option["id"])
        if is_correct:
            score += 1
        result_items.append(
            {
                "id": question["id"],
                "prompt": question["prompt"],
                "selectedOptionId": selected_option["id"] if selected_option else None,
                "selectedLabel": selected_option["label"] if selected_option else None,
                "correctOptionId": correct_option["id"] if correct_option else None,
                "correctLabel": correct_option["label"] if correct_option else None,
                "correct": is_correct,
                "explanation": question["explanation"],
                "topic": question["topic"],
            }
        )

    passed = score >= READINESS_PASS_SCORE
    current_user_id = _current_user_id()
    passed_at = datetime.utcnow() if passed else None

    if current_user_id:
        record, created = ReadinessQuizResult.get_or_create(
            user=current_user_id,
            defaults={
                "passed": passed,
                "score": score,
                "total_questions": len(question_set),
                "passed_at": passed_at,
                "answers_json": json.dumps(result_items, ensure_ascii=False),
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow(),
            },
        )
        if not created:
            record.passed = passed
            record.score = score
            record.total_questions = len(question_set)
            record.passed_at = passed_at
            record.answers_json = json.dumps(result_items, ensure_ascii=False)
            record.updated_at = datetime.utcnow()
            record.save()
        storage = "server"
    else:
        session["readiness_guest"] = {
            "passed": passed,
            "score": score,
            "total_questions": len(question_set),
            "passed_at": passed_at.isoformat() + "Z" if passed_at else None,
        }
        session.modified = True
        storage = "session"

    _clear_readiness_question_set()

    return jsonify(
        {
            "passed": passed,
            "score": score,
            "total_questions": len(question_set),
            "pass_score": READINESS_PASS_SCORE,
            "results": result_items,
            "storage": storage,
            "can_access_career": passed,
            "user_authenticated": bool(current_user_id),
            "guest": _is_guest_user(),
        }
    )


# ----------------------
#   Health
# ----------------------
@bp.get("/health")
def health():
    return jsonify(status="ok")


@bp.get("/favicon.ico")
def favicon():
    static_dir = Path(__file__).resolve().parent / "static" / "img"
    return send_from_directory(static_dir, "favicon.png")


# ----------------------
#   Datos de empresas
# ----------------------
DATA_PATH = Path(__file__).resolve().parent / "data" / "empresas.json"


def _cargar_empresas():
    with DATA_PATH.open("r", encoding="utf-8-sig") as f:
        data = json.load(f)
    for e in data:
        assert {"ticker", "nombre", "sector"} <= set(e.keys())
    return data


EMPRESAS = _cargar_empresas()


def _norm(s: str) -> str:
    if not isinstance(s, str):
        return ""
    nfkd = unicodedata.normalize("NFKD", s)
    return "".join(ch for ch in nfkd if not unicodedata.combining(ch)).lower()


@bp.get("/empresas/sectores")
def listar_sectores():
    sectores = sorted(
        {(e.get("sector") or "").strip() for e in EMPRESAS if e.get("sector")}
    )
    return jsonify(sectores)


@bp.get("/empresas-data")
def listar_empresas():
    """
    Devuelve lista de empresas.
    Filtros opcionales:
      - ?sector=... -> igualdad exacta normalizada
      - ?q=... -> búsqueda parcial en ticker o nombre
      - ?page&per_page ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ (opcional) si se envÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â­an, responde paginado
    """
    sector = request.args.get("sector")
    q = request.args.get("q")

    resultado = EMPRESAS

    if sector:
        target = _norm(sector)
        resultado = [e for e in resultado if _norm(e.get("sector", "")) == target]

    if q:
        needle = _norm(q)

        def coincide(e):
            return needle in _norm(e.get("ticker", "")) or needle in _norm(
                e.get("nombre", "")
            )

        resultado = [e for e in resultado if coincide(e)]

    # Solo paginar si el cliente lo pide
    page = request.args.get("page")
    per_page = request.args.get("per_page")
    if page or per_page:
        return jsonify(_paginate(resultado, page, per_page))
    return jsonify(resultado)


# ----------------------
#   Motor de análisis
# ----------------------
def _validar_payload(p):
    errores = []

    ticker = p.get("ticker")
    if not ticker or not isinstance(ticker, str):
        errores.append("Falta 'ticker' (string).")

    importe = p.get("importe_inicial")
    if not isinstance(importe, (int, float)) or importe <= 0:
        errores.append("'importe_inicial' debe ser numerico > 0.")

    horizonte = p.get("horizonte_anios")
    if horizonte is None:
        errores.append("Falta el campo 'horizonte_anios'.")
    elif not isinstance(horizonte, int):
        errores.append("El campo 'horizonte_anios' debe ser un entero.")
    elif horizonte < 1:
        errores.append(
            "Horizonte mÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â­nimo: 1 aÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â±o (horizonte_anios >= 1)."
        )

    sup = p.get("supuestos") or {}
    if not isinstance(sup, dict):
        errores.append("'supuestos' debe ser un objeto con porcentajes.")
        sup = {}
    else:
        p["supuestos"] = sup

    def pct_ok(clave, minimo, maximo):
        if clave not in sup:
            return None
        valor = sup.get(clave)
        if valor is None:
            return None
        if not isinstance(valor, (int, float)):
            errores.append(f"'{clave}' debe ser numerico.")
            return None
        if valor < minimo or valor > maximo:
            errores.append(f"'{clave}' debe estar entre {minimo} y {maximo}.")
        return valor

    pct_ok("crecimiento_anual_pct", 0, 100)
    pct_ok("margen_seguridad_pct", 0, 100)
    pct_ok("roe_pct", 0, 100)
    pct_ok("deuda_sobre_activos_pct", 0, 100)

    just = p.get("justificacion")
    if just is not None and not isinstance(just, str):
        errores.append("'justificacion' debe ser texto.")
    elif isinstance(just, str) and len(just.strip()) < 5:
        errores.append("La 'justificacion' debe tener al menos 5 caracteres.")

    modo = p.get("modo") or "SIN_DCA"
    if modo not in {"DCA", "SIN_DCA"}:
        errores.append("'modo' debe ser 'DCA' o 'SIN_DCA'.")
    elif modo == "DCA":
        dca = p.get("dca") or {}
        if not isinstance(dca, dict):
            errores.append("'dca' debe ser un objeto con aporte y frecuencia.")
            dca = {}
        aporte = dca.get("aporte")
        if aporte is None or not isinstance(aporte, (int, float)) or aporte < 0:
            errores.append("'dca.aporte' no puede ser negativo.")
        frecuencia = (dca.get("frecuencia") or "").upper()
        if frecuencia not in {"WEEKLY", "MONTHLY", "QUARTERLY", "ANNUAL"}:
            errores.append("'dca.frecuencia' no es valida.")
    else:
        p["dca"] = None

    crec = sup.get("crecimiento_anual_pct")
    if isinstance(crec, (int, float)) and crec > 25:
        errores.append("Crecimiento anual > 25% sostenido es probablemente irrealista.")

    return errores


def _normalizar_payload(datos):
    datos = dict(datos or {})

    ticker = datos.get("ticker")
    if isinstance(ticker, str):
        datos["ticker"] = ticker.strip().upper()

    def to_float(value):
        if value in (None, ""):
            return None
        try:
            return float(value)
        except (TypeError, ValueError):
            return None

    if "importe_inicial" in datos:
        imp = to_float(datos.get("importe_inicial"))
        if imp is not None:
            datos["importe_inicial"] = imp if not imp.is_integer() else int(imp)

    if "horizonte_anios" in datos:
        try:
            datos["horizonte_anios"] = int(round(float(datos["horizonte_anios"])))
        except (TypeError, ValueError):
            pass

    sup_in = datos.get("supuestos")
    sup = dict(sup_in) if isinstance(sup_in, dict) else {}

    mapping = {
        "crecimiento_anual_estimado": "crecimiento_anual_pct",
        "margen_seguridad_pct": "margen_seguridad_pct",
        "roe_pct": "roe_pct",
        "deuda_sobre_activos_pct": "deuda_sobre_activos_pct",
    }
    for origen, destino in mapping.items():
        if origen in datos and destino not in sup:
            sup[destino] = datos[origen]

    for clave in (
        "crecimiento_anual_pct",
        "margen_seguridad_pct",
        "roe_pct",
        "deuda_sobre_activos_pct",
    ):
        val = to_float(sup.get(clave))
        sup[clave] = 0.0 if val is None else val

    datos["supuestos"] = sup

    modo = datos.get("modo")
    if modo not in {"DCA", "SIN_DCA"}:
        modo = "SIN_DCA"
    datos["modo"] = modo

    if modo == "DCA":
        dca = datos.get("dca")
        if not isinstance(dca, dict):
            dca = {}
        aporte = to_float(dca.get("aporte"))
        aporte_norm = 0.0 if aporte is None else aporte
        if isinstance(aporte_norm, float) and aporte_norm.is_integer():
            aporte_norm = int(aporte_norm)
        frecuencia = (dca.get("frecuencia") or "MONTHLY").upper()
        datos["dca"] = {"aporte": aporte_norm, "frecuencia": frecuencia}
    else:
        datos["dca"] = None

    just = datos.get("justificacion")
    if just is not None and not isinstance(just, str):
        datos["justificacion"] = str(just)

    if "crecimiento_anual_estimado" in datos:
        ce = to_float(datos["crecimiento_anual_estimado"])
        datos["crecimiento_anual_estimado"] = (
            ce if ce is not None else sup.get("crecimiento_anual_pct")
        )
    else:
        datos["crecimiento_anual_estimado"] = sup.get("crecimiento_anual_pct")

    if "margen_seguridad_pct" in datos:
        ms = to_float(datos["margen_seguridad_pct"])
        datos["margen_seguridad_pct"] = (
            ms if ms is not None else sup.get("margen_seguridad_pct")
        )
    else:
        datos["margen_seguridad_pct"] = sup.get("margen_seguridad_pct")

    for key in ("inicio", "fin"):
        val = datos.get(key)
        if isinstance(val, str):
            val = val.strip()
            datos[key] = val or None
        elif val not in (None,):
            datos[key] = str(val)

    return datos


def _puntuar_y_observar(p):
    """Heurística muy simple para MVP: 0–100."""
    sup = p["supuestos"]
    horizon = p["horizonte_anios"]

    score = 50
    obs = []

    # Horizonte
    if horizon >= 10:
        score += 10
        obs.append({"tipo": "ok", "msg": "Horizonte largo (≥10 años)."})
    elif horizon >= 5:
        score += 5
        obs.append({"tipo": "ok", "msg": "Horizonte adecuado (≥5 años)."})

    # ROE
    roe = sup.get("roe_pct", 0)
    if roe >= 15:
        score += 10
    elif roe >= 8:
        score += 5

    # Deuda
    deuda = sup.get("deuda_sobre_activos_pct", 0)
    if deuda <= 30:
        score += 10
    elif deuda <= 60:
        score += 3
    else:
        score -= 5

    # Margen de seguridad
    margen = sup.get("margen_seguridad_pct", 0)
    if margen >= 20:
        score += 10
        obs.append({"tipo": "ok", "msg": "Margen de seguridad sólido (≥20%)."})
    elif margen >= 10:
        score += 3
        obs.append(
            {"tipo": "mejora", "msg": "Margen de seguridad algo justo (10–20%)."}
        )
    else:
        score -= 5
        obs.append({"tipo": "alerta", "msg": "Margen de seguridad bajo (<10%)."})

    # Crecimiento
    crec = sup.get("crecimiento_anual_pct", 0)
    if crec > 25:
        score -= 10
        obs.append(
            {
                "tipo": "alerta",
                "msg": "Supuesto de crecimiento >25% parece optimista/irrealista.",
            }
        )
    elif crec >= 5:
        score += 5
        obs.append({"tipo": "ok", "msg": "Crecimiento razonable (5–25%)."})
    else:
        obs.append(
            {"tipo": "mejora", "msg": "Crecimiento bajo: compénsalo con precio/margen."}
        )

    # Justificación
    if len((p.get("justificacion") or "").strip()) >= 60:
        score += 5
        obs.append({"tipo": "ok", "msg": "Buena justificación (detallada)."})
    else:
        obs.append(
            {
                "tipo": "mejora",
                "msg": "Amplía la justificación: riesgos, sensibilidad, comparables.",
            }
        )

    score = max(0, min(100, int(round(score))))

    if score >= 80:
        resumen = "Análisis sólido."
    elif score >= 60:
        resumen = "Análisis razonable con áreas de mejora."
    else:
        resumen = "Análisis débil: revisa supuestos, riesgos y valoración."

    return score, obs, resumen


# ----------------------
#   Persistencia análisis


def _fix_mojibake(s):
    if not isinstance(s, str):
        return s
    if "Ã" not in s and "Â" not in s:
        return s
    try:
        return s.encode("latin-1").decode("utf-8")
    except Exception:
        return s


def _sanear_registro(r: dict) -> dict:
    if not isinstance(r, dict):
        return r
    if "resumen" in r:
        r["resumen"] = _fix_mojibake(r["resumen"])
    if isinstance(r.get("observaciones"), list):
        out = []
        for o in r["observaciones"]:
            if not isinstance(o, dict):
                continue
            msg = _fix_mojibake(o.get("msg", ""))
            if any(k in msg.lower() for k in ("roe", "deuda")):
                continue
            out.append({**o, "msg": msg})
        r["observaciones"] = out
    return r


# ----------------------

DATA_DIR = Path(__file__).resolve().parent / "data"
ANALISIS_PATH = DATA_DIR / "analisis.json"


def _cargar_lista(path: Path):
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []
    if isinstance(data, list):
        data = [_sanear_registro(x) for x in data]
    return data


def _guardar_lista(path: Path, lista):
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(lista, list):
        lista = [_sanear_registro(x) for x in lista]
    with path.open("w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=2)


def _current_user_id():
    user_id = session.get("user_id")
    user = get_user_by_id(user_id)
    return user.id if user else None


def _is_guest_user():
    return bool(session.get("guest"))


def _registrar_analisis(datos):
    errores = _validar_payload(datos)
    if errores:
        return jsonify({"valido": False, "errores": errores}), 400

    puntuacion, observaciones, resumen = _puntuar_y_observar(datos)

    registro = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "ticker": datos.get("ticker"),
        "importe_inicial": datos.get("importe_inicial"),
        "horizonte_anios": datos.get("horizonte_anios"),
        "supuestos": datos.get("supuestos", {}),
        "justificacion": datos.get("justificacion", ""),
        "modo": datos.get("modo"),
        "dca": datos.get("dca"),
        "crecimiento_anual_estimado": datos.get("crecimiento_anual_estimado"),
        "margen_seguridad_pct": datos.get("margen_seguridad_pct"),
        "puntuacion": puntuacion,
        "observaciones": observaciones,
        "resumen": resumen,
    }

    registro["inicio"] = datos.get("inicio")
    registro["fin"] = datos.get("fin")

    backtest_payload = {
        "ticker": registro.get("ticker"),
        "importe_inicial": registro.get("importe_inicial"),
        "horizonte_anios": registro.get("horizonte_anios"),
        "modo": registro.get("modo"),
        "dca": registro.get("dca"),
        "inicio": registro.get("inicio"),
        "fin": registro.get("fin"),
    }
    backtest_snapshot = None
    try:
        backtest_snapshot = _market_backtest_core(backtest_payload)
    except BacktestError:
        backtest_snapshot = None
    except Exception:
        backtest_snapshot = None

    registro["backtest"] = backtest_snapshot

    registro = _sanear_registro(registro)

    user_id = _current_user_id()
    if user_id and not _is_guest_user():
        save_analysis_for_user(
            user_id=user_id,
            ticker=registro.get("ticker"),
            payload={
                "importe_inicial": registro.get("importe_inicial"),
                "horizonte_anios": registro.get("horizonte_anios"),
                "supuestos": registro.get("supuestos", {}),
                "justificacion": registro.get("justificacion", ""),
                "modo": registro.get("modo"),
                "dca": registro.get("dca"),
                "crecimiento_anual_estimado": registro.get("crecimiento_anual_estimado"),
                "margen_seguridad_pct": registro.get("margen_seguridad_pct"),
                "inicio": registro.get("inicio"),
                "fin": registro.get("fin"),
            },
            result={
                "puntuacion": registro.get("puntuacion"),
                "observaciones": registro.get("observaciones"),
                "resumen": registro.get("resumen"),
                "backtest": registro.get("backtest"),
            },
        )

    return jsonify(
        {
            "valido": True,
            "puntuacion": puntuacion,
            "observaciones": observaciones,
            "resumen": resumen,
            "registro": {
                "id": registro["id"],
                "timestamp": registro["timestamp"],
                "ticker": registro["ticker"],
                "importe_inicial": registro["importe_inicial"],
                "horizonte_anios": registro["horizonte_anios"],
                "modo": registro["modo"],
                "dca": registro["dca"],
            },
        }
    )


@bp.post("/analisis")
def crear_analisis():
    datos_brutos = request.get_json(silent=True) or {}
    datos = _normalizar_payload(datos_brutos)
    return _registrar_analisis(datos)


@bp.post("/api/propuestas")
def crear_propuesta_api():
    datos_brutos = request.get_json(silent=True) or {}
    datos = _normalizar_payload(datos_brutos)
    return _registrar_analisis(datos)


@bp.get("/analisis")
def listar_analisis():
    """
    Devuelve el historial de análisis, mostrando primero los más recientes.
    Filtros opcionales (se aplican ANTES del paginado):
      - ?ticker=MSFT      (case-insensitive, igualdad exacta)
      - ?desde=YYYY-MM-DD (inclusive por fecha de timestamp)
      - ?hasta=YYYY-MM-DD (exclusivo del dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â­a siguiente; simplificamos usando prefijos)
    Paginado opcional:
      - ?page, ?per_page
    """
    user_id = _current_user_id()
    if _is_guest_user():
        return jsonify({"error": "El modo invitado no dispone de historial guardado."}), 403
    if not user_id:
        return jsonify({"error": "Debes iniciar sesión para consultar tu historial."}), 401

    ticker = request.args.get("ticker")
    desde = request.args.get("desde")
    hasta = request.args.get("hasta")
    historial = list_analysis_for_user(user_id, ticker=ticker, desde=desde, hasta=hasta)

    page = request.args.get("page")
    per_page = request.args.get("per_page")
    if page or per_page:
        return jsonify(_paginate(historial, page, per_page))
    return jsonify(historial)


@bp.get("/analisis.csv")
def exportar_analisis_csv():
    """
    Exporta el historial de análisis en CSV (UTF-8 con BOM para Excel).
    Acepta los mismos filtros que GET /analisis: ?ticker, ?desde, ?hasta
    """
    user_id = _current_user_id()
    if _is_guest_user():
        return jsonify({"error": "El modo invitado no permite exportar historial."}), 403
    if not user_id:
        return jsonify({"error": "Debes iniciar sesión para exportar tu historial."}), 401

    ticker = request.args.get("ticker")
    desde = request.args.get("desde")
    hasta = request.args.get("hasta")
    historial = list_analysis_for_user(user_id, ticker=ticker, desde=desde, hasta=hasta)

    headers = [
        "id",
        "timestamp",
        "ticker",
        "importe_inicial",
        "horizonte_anios",
        "puntuacion",
        "resumen",
    ]

    has_backtest = any(h.get("backtest") for h in historial)
    if has_backtest:
        headers += ["bt_start", "bt_end", "bt_invested", "bt_final", "bt_pnl_pct"]

    out = io.StringIO()
    w = csv.writer(out, lineterminator="\n")
    w.writerow(headers)
    for h in historial:
        row = [
            h.get("id", ""),
            h.get("timestamp", ""),
            h.get("ticker", ""),
            h.get("importe_inicial", ""),
            h.get("horizonte_anios", ""),
            h.get("puntuacion", ""),
            (h.get("resumen", "") or "").replace("\n", " ").strip(),
        ]
        if has_backtest:
            bt = h.get("backtest") or {}
            row.extend(
                [
                    bt.get("start") or "",
                    bt.get("end") or "",
                    bt.get("invested") if bt.get("invested") is not None else "",
                    bt.get("final_value") if bt.get("final_value") is not None else "",
                    bt.get("pnl_pct") if bt.get("pnl_pct") is not None else "",
                ]
            )
        w.writerow(row)

    # Añadimos BOM para que Excel detecte UTF-8 automáticamente
    csv_text = "\ufeff" + out.getvalue()

    return Response(
        csv_text,
        headers={
            "Content-Disposition": 'attachment; filename="analisis.csv"',
            "Content-Type": "text/csv; charset=utf-8",
        },
        status=200,
    )


# ----------------------
#   Helpers generales
# ----------------------


def _paginate(lista, page: str | None, per_page: str | None):
    p = int(page) if page and page.isdigit() and int(page) > 0 else 1
    pp = int(per_page) if per_page and per_page.isdigit() and int(per_page) > 0 else 10
    total = len(lista)
    start = (p - 1) * pp
    end = start + pp
    items = lista[start:end]
    has_next = end < total
    return {
        "items": items,
        "page": p,
        "per_page": pp,
        "total": total,
        "has_next": has_next,
    }


def _parse_date_yyyy_mm_dd(s: str | None):
    if not s:
        return None
    try:
        from datetime import datetime

        # interpretamos fecha en UTC a medianoche
        return datetime.fromisoformat(s)
    except Exception:
        return None


def _filtrar_analisis(
    historial, ticker: str | None, desde: str | None, hasta: str | None
):
    if ticker:
        tnorm = _norm(ticker)
        historial = [h for h in historial if _norm(h.get("ticker", "")) == tnorm]
    if desde:
        historial = [h for h in historial if h.get("timestamp", "")[:10] >= desde]
    if hasta:
        historial = [h for h in historial if h.get("timestamp", "")[:10] < hasta]
    return historial


# --- Yahoo Finance: Datos de mercado y backtest ---
def _parse_iso_date(value: str | None) -> date | None:
    if not value:
        return None
    try:
        return pd.to_datetime(value).date()
    except Exception:
        return None


def _as_bool(value: str | None, default: bool = True) -> bool:
    if value is None:
        return default
    return str(value).strip().lower() in {"1", "true", "t", "yes", "y"}


def _normalize_price_df(df: pd.DataFrame) -> pd.DataFrame:
    if df is None or df.empty:
        return df
    if isinstance(df.columns, pd.MultiIndex):
        df = df.copy()
        df.columns = df.columns.get_level_values(0)
    return df


def _extract_series(df: pd.DataFrame, column: str, ticker: str) -> pd.Series:
    if df is None or df.empty or column not in df:
        return pd.Series(dtype=float)
    series = df[column].copy()
    if isinstance(series, pd.DataFrame):
        if ticker in series.columns:
            series = series[ticker]
        else:
            series = series.iloc[:, 0]
    return series


def _series_with_date_index(series: pd.Series) -> pd.Series:
    series = series.copy()
    if not series.empty:
        series.index = pd.to_datetime(series.index).date
    return series


def _series_to_map(series: pd.Series) -> dict[str, float | None]:
    return {
        str(idx): (None if pd.isna(val) else float(val)) for idx, val in series.items()
    }


def _first_price_on_or_after(series: pd.Series, target: date) -> float | None:
    if series.empty:
        return None
    for idx, value in series.sort_index().items():
        if idx >= target and not pd.isna(value):
            return float(value)
    return None


def _last_price_on_or_before(series: pd.Series, target: date) -> float | None:
    if series.empty:
        return None
    for idx in series.sort_index().index[::-1]:
        value = series.loc[idx]
        if idx <= target and not pd.isna(value):
            return float(value)
    return None


def _round_or_none(value: float | None, digits: int) -> float | None:
    if value is None:
        return None
    return round(value, digits)


class BacktestError(Exception):
    def __init__(self, message: str, status_code: int = 400):
        super().__init__(message)
        self.status_code = status_code


class HorizonSimulationError(Exception):
    def __init__(self, message: str, status_code: int = 400, warnings: list[str] | None = None):
        super().__init__(message)
        self.status_code = status_code
        self.warnings = warnings or []


def _download_history_df(
    ticker: str, start_d: date, end_d: date, include_actions: bool = True
) -> pd.DataFrame:
    ticker_clean = (ticker or "").strip()
    not_found_msg = (
        f"No se encontraron datos para el ticker '{ticker_clean}'. "
        "Asegúrate de usar el símbolo bursátil (ej: AAPL) y no el nombre de la empresa."
    )
    if not ticker_clean:
        raise BacktestError(not_found_msg, 404)

    try:
        df = yf.download(
            ticker_clean,
            start=str(start_d),
            end=str(end_d + timedelta(days=1)),
            interval="1d",
            auto_adjust=False,
            actions=include_actions,
            progress=False,
        )
    except YFRateLimitError as exc:
        raise BacktestError(
            "No se pudieron obtener datos del activo en este momento. La fuente de mercado ha limitado temporalmente las peticiones. Prueba de nuevo dentro de unos segundos o utiliza otro activo.",
            503,
        ) from exc
    except Exception as exc:
        raise BacktestError(
            f"No se pudieron obtener datos de mercado para '{ticker_clean}' en este momento.",
            503,
        ) from exc

    df = _normalize_price_df(df)
    if df is None or df.empty:
        raise BacktestError(not_found_msg, 404)
    return df


def _extract_market_price_series(df: pd.DataFrame, ticker: str) -> pd.Series:
    normalized_df = _normalize_price_df(df)
    series = _extract_series(normalized_df, "Adj Close", ticker)
    if series.empty:
        series = _extract_series(normalized_df, "Close", ticker)
    if isinstance(series, pd.DataFrame):
        series = series.iloc[:, 0] if not series.empty else pd.Series(dtype=float)
    if series is None:
        return pd.Series(dtype=float)

    series = pd.to_numeric(pd.Series(series).copy(), errors="coerce").dropna()
    if series.empty:
        return pd.Series(dtype=float)

    datetime_index = pd.to_datetime(series.index, errors="coerce")
    valid_mask = ~pd.isna(datetime_index)
    series = series.loc[valid_mask]
    datetime_index = datetime_index[valid_mask]
    if series.empty:
        return pd.Series(dtype=float)

    series.index = pd.DatetimeIndex(datetime_index)
    series = series[~series.index.duplicated(keep="last")].sort_index()
    if not isinstance(series.index, pd.DatetimeIndex):
        return pd.Series(dtype=float)
    return series


def _compute_horizon_monthly_returns(df: pd.DataFrame, ticker: str) -> pd.Series:
    series = _extract_market_price_series(df, ticker)
    if series.empty:
        raise HorizonSimulationError(
            f"{ticker} no dispone de una serie temporal válida para construir la simulación experimental.",
            400,
        )
    monthly = series.resample("ME").last().pct_change().dropna()
    if monthly.empty:
        raise HorizonSimulationError(
            f"{ticker} no genera retornos mensuales suficientes para esta simulación experimental.",
            400,
        )
    return monthly


def _compute_price_summary(
    ticker: str, start_d: date, end_d: date, df: pd.DataFrame
) -> dict:
    adj = _series_with_date_index(_extract_series(df, "Adj Close", ticker))
    close = _series_with_date_index(_extract_series(df, "Close", ticker))
    dividends = _series_with_date_index(_extract_series(df, "Dividends", ticker))

    if adj.empty and close.empty:
        raise BacktestError("Sin datos de precios para el rango solicitado", 404)

    notes: list[str] = []

    start_price_adj = _first_price_on_or_after(adj, start_d)
    if start_price_adj is None:
        notes.append("Precio inicial ajustado no disponible en el rango")

    end_price_adj = _last_price_on_or_before(adj, end_d)
    if end_price_adj is None:
        notes.append("Precio final ajustado no disponible en el rango")

    start_price = _first_price_on_or_after(close, start_d)
    if start_price is None:
        notes.append("Precio inicial sin ajustar no disponible en el rango")

    end_price = _last_price_on_or_before(close, end_d)
    if end_price is None:
        notes.append("Precio final sin ajustar no disponible en el rango")

    variation_adj_pct = None
    if start_price_adj and end_price_adj and start_price_adj != 0:
        variation_adj_pct = (end_price_adj / start_price_adj - 1) * 100

    variation_raw_pct = None
    if start_price and end_price and start_price != 0:
        variation_raw_pct = (end_price / start_price - 1) * 100

    has_dividends = (
        bool(dividends.fillna(0).ne(0).any()) if not dividends.empty else False
    )

    now_price = None
    try:
        fast_info = yf.Ticker(ticker).fast_info
        candidate = getattr(fast_info, "last_price", None)
        if candidate is not None and not (
            isinstance(candidate, float) and math.isnan(candidate)
        ):
            now_price = float(candidate)
    except Exception:
        now_price = None

    if now_price is None:
        fallback = end_price_adj if end_price_adj is not None else None
        if fallback is None and not adj.dropna().empty:
            fallback = float(adj.dropna().iloc[-1])
        if fallback is not None:
            now_price = fallback
            notes.append("Tiempo real no disponible; se usa ultimo cierre ajustado")
        else:
            notes.append("Tiempo real no disponible")

    return {
        "start_price_adj": _round_or_none(start_price_adj, 4),
        "end_price_adj": _round_or_none(end_price_adj, 4),
        "variation_adj_pct": _round_or_none(variation_adj_pct, 2),
        "start_price": _round_or_none(start_price, 4),
        "end_price": _round_or_none(end_price, 4),
        "variation_raw_pct": _round_or_none(variation_raw_pct, 2),
        "now_price": _round_or_none(now_price, 4) if now_price is not None else None,
        "has_dividends": has_dividends,
        "notes": notes,
        "adj_series": adj,
    }


def _iso(d):
    if pd.isna(d):
        return None
    return str(pd.to_datetime(d).date())


@bp.get("/market/ohlc/<ticker>")
def market_ohlc(ticker):
    """
    Devuelve OHLCV + Adj Close para un ticker.
    Query params:
      - start=YYYY-MM-DD
      - end=YYYY-MM-DD
      - interval=1d|1wk|1mo (default 1d)
    Respuesta: lista de objetos {date, open, high, low, close, adj_close, volume}
    """
    t = (ticker or "").strip()
    if not t:
        return jsonify({"error": "Ticker requerido"}), 400

    start = request.args.get("start")
    end = request.args.get("end")
    interval = request.args.get("interval", "1d")

    try:
        df = yf.download(
            t,
            start=start,
            end=end,
            interval=interval,
            auto_adjust=False,
            progress=False,
        )
        if df is None or df.empty:
            return jsonify([])

        df = _normalize_price_df(df)

        df = df.rename(
            columns={
                "Open": "open",
                "High": "high",
                "Low": "low",
                "Close": "close",
                "Adj Close": "adj_close",
                "Volume": "volume",
            }
        ).reset_index()

        rows = []
        for _, r in df.iterrows():
            rows.append(
                {
                    "date": _iso(r.get("Date")),
                    "open": None if pd.isna(r.get("open")) else float(r.get("open")),
                    "high": None if pd.isna(r.get("high")) else float(r.get("high")),
                    "low": None if pd.isna(r.get("low")) else float(r.get("low")),
                    "close": None if pd.isna(r.get("close")) else float(r.get("close")),
                    "adj_close": (
                        None
                        if pd.isna(r.get("adj_close"))
                        else float(r.get("adj_close"))
                    ),
                    "volume": (
                        None if pd.isna(r.get("volume")) else int(r.get("volume"))
                    ),
                }
            )
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def _gen_schedule(start_date: date, end_date: date, freq: str):
    step = {"WEEKLY": 7, "MONTHLY": 30, "QUARTERLY": 91, "ANNUAL": 365}.get(
        (freq or "").upper(), 30
    )
    d = start_date
    while d <= end_date:
        yield d
        d = d + timedelta(days=step)


def _nearest_trading_close(adj_close_by_day: dict, d: date):
    # busca el primer dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â­a con dato >= fecha objetivo (forward fill hacia adelante)
    for i in range(0, 14):
        k = str(d + timedelta(days=i))
        v = adj_close_by_day.get(k)
        if v is not None:
            return float(v)
    return None


def _market_backtest_core(payload: dict) -> dict:
    t = (payload.get("ticker") or "").strip().upper()
    if not t:
        raise BacktestError("Ticker requerido", 400)

    try:
        horizon = int(payload.get("horizonte_anios") or 0)
    except (TypeError, ValueError):
        raise BacktestError("Horizonte invalido", 400)
    if horizon < 1:
        raise BacktestError("Horizonte >= 1 año", 400)

    try:
        invested_initial = float(payload.get("importe_inicial") or 0)
    except (TypeError, ValueError):
        invested_initial = 0.0
    if invested_initial <= 0:
        raise BacktestError("Importe inicial debe ser mayor a 0", 400)

    modo = (payload.get("modo") or "SIN_DCA").upper()
    if modo not in {"DCA", "SIN_DCA"}:
        modo = "SIN_DCA"

    dca = payload.get("dca") or {}
    aporte = 0.0
    freq = "MONTHLY"
    if modo == "DCA" and isinstance(dca, dict):
        try:
            aporte = float(dca.get("aporte") or 0.0)
        except (TypeError, ValueError):
            aporte = 0.0
        if aporte < 0:
            raise BacktestError("Aporte DCA no puede ser negativo", 400)
        freq = (dca.get("frecuencia") or "MONTHLY").upper()

    today = date.today()
    start_raw = payload.get("inicio")
    if start_raw:
        start_d = _parse_iso_date(start_raw)
        if not start_d:
            raise BacktestError("Fecha de inicio invalida", 400)
    else:
        try:
            start_d = today.replace(year=today.year - horizon)
        except ValueError:
            start_d = today - timedelta(days=365 * horizon)

    end_raw = payload.get("fin")
    if end_raw:
        end_d = _parse_iso_date(end_raw)
        if not end_d:
            raise BacktestError("Fecha de fin invalida", 400)
    else:
        end_d = today

    if end_d < start_d:
        raise BacktestError(
            "La fecha de fin debe ser posterior o igual a la inicial", 400
        )

    df = _download_history_df(t, start_d, end_d, include_actions=True)
    if df is None or df.empty:
        raise BacktestError("Sin datos para el rango solicitado", 404)

    metrics = _compute_price_summary(t, start_d, end_d, df)
    adj = metrics.get("adj_series")
    if adj is None or adj.empty:
        raise BacktestError("Sin datos de precios ajustados", 404)

    adj_map = _series_to_map(adj)

    first_px = _nearest_trading_close(adj_map, start_d)
    if first_px is None:
        raise BacktestError("No hay precio inicial cercano", 404)

    invested = invested_initial
    shares = invested / first_px if first_px else 0.0

    if modo == "DCA" and aporte > 0:
        for d in _gen_schedule(start_d + timedelta(days=1), end_d, freq):
            px = _nearest_trading_close(adj_map, d)
            if px:
                invested += aporte
                shares += aporte / px

    last_px = _last_price_on_or_before(adj, end_d)
    if last_px is None and not adj.dropna().empty:
        last_px = float(adj.dropna().iloc[-1])
    if last_px is None:
        raise BacktestError("No hay precio final disponible", 404)

    final_value = shares * last_px
    pnl_abs = final_value - invested
    pnl_pct = (pnl_abs / invested) * 100 if invested > 0 else 0.0

    result = {
        "ticker": t,
        "start": str(start_d),
        "end": str(end_d),
        "desde": str(start_d),
        "hasta": str(end_d),
        "invested": _round_or_none(invested, 2),
        "shares": float(shares),
        "last_price": _round_or_none(last_px, 4),
        "final_value": _round_or_none(final_value, 2),
        "pnl_abs": _round_or_none(pnl_abs, 2),
        "pnl_pct": _round_or_none(pnl_pct, 2),
        "modo": modo,
        "start_price_adj": metrics["start_price_adj"],
        "end_price_adj": metrics["end_price_adj"],
        "variation_adj_pct": metrics["variation_adj_pct"],
        "start_price": metrics["start_price"],
        "end_price": metrics["end_price"],
        "variation_raw_pct": metrics["variation_raw_pct"],
        "now_price": metrics["now_price"],
        "has_dividends": metrics["has_dividends"],
        "notes": metrics["notes"],
    }

    metrics.pop("adj_series", None)
    return result


@bp.post("/market/backtest")
def market_backtest():
    """
    Calcula el resultado real de una inversión usando precios ajustados (Adj Close).
    Body JSON esperado:
    {
      "ticker": "AAPL",
      "importe_inicial": 1000,
      "horizonte_anios": 3,
      "modo": "DCA"|"SIN_DCA",
      "dca": {"aporte": 100, "frecuencia": "MONTHLY"} | null,
      "inicio": "YYYY-MM-DD" (opcional; por defecto hoy - horizonte_anios),
      "fin": "YYYY-MM-DD" (opcional; por defecto hoy)
    }
    """
    payload = request.get_json(silent=True) or {}
    try:
        result = _market_backtest_core(payload)
        return jsonify(result)
    except BacktestError as exc:
        return jsonify({"error": str(exc)}), exc.status_code
    except Exception as exc:  # noqa: BLE001
        return jsonify({"error": str(exc)}), 500


@bp.get("/market/summary")
def market_summary():
    t = (request.args.get("ticker") or "").strip().upper()
    if not t:
        return jsonify({"error": "Ticker requerido"}), 400

    start_raw = request.args.get("start")
    if not start_raw:
        return jsonify({"error": "Parametro start requerido"}), 400
    start_d = _parse_iso_date(start_raw)
    if not start_d:
        return jsonify({"error": "Fecha de inicio invalida"}), 400

    end_raw = request.args.get("end")
    if end_raw:
        end_d = _parse_iso_date(end_raw)
        if not end_d:
            return jsonify({"error": "Fecha de fin invalida"}), 400
    else:
        end_d = date.today()

    if end_d < start_d:
        return (
            jsonify(
                {"error": "La fecha de fin debe ser posterior o igual a la inicial"}
            ),
            400,
        )

    # adjusted = _as_bool(request.args.get("adjusted"), True) # no usado

    df = _download_history_df(t, start_d, end_d, include_actions=True)
    if df is None or df.empty:
        return jsonify({"error": "Sin datos para el rango solicitado"}), 404

    try:
        metrics = _compute_price_summary(t, start_d, end_d, df)
    except BacktestError as exc:
        return jsonify({"error": str(exc)}), exc.status_code

    metrics.pop("adj_series", None)

    response = {
        "ticker": t,
        "start": str(start_d),
        "end": str(end_d),
        "start_price_adj": metrics["start_price_adj"],
        "end_price_adj": metrics["end_price_adj"],
        "variation_adj_pct": metrics["variation_adj_pct"],
        "start_price": metrics["start_price"],
        "end_price": metrics["end_price"],
        "variation_raw_pct": metrics["variation_raw_pct"],
        "now_price": metrics["now_price"],
        "has_dividends": metrics["has_dividends"],
        "notes": metrics["notes"],
    }
    return jsonify(response)


@bp.get("/market/ohlc_csv")
def market_ohlc_csv():
    t = (request.args.get("ticker") or "").strip().upper()
    if not t:
        return jsonify({"error": "Ticker requerido"}), 400

    start_raw = request.args.get("start")
    if not start_raw:
        return jsonify({"error": "Parametro start requerido"}), 400
    start_d = _parse_iso_date(start_raw)
    if not start_d:
        return jsonify({"error": "Fecha de inicio invalida"}), 400

    end_raw = request.args.get("end")
    if end_raw:
        end_d = _parse_iso_date(end_raw)
        if not end_d:
            return jsonify({"error": "Fecha de fin invalida"}), 400
    else:
        end_d = date.today()

    if end_d < start_d:
        return (
            jsonify(
                {"error": "La fecha de fin debe ser posterior o igual a la inicial"}
            ),
            400,
        )

    adjusted = _as_bool(request.args.get("adjusted"), True)

    df = yf.download(
        t,
        start=str(start_d),
        end=str(end_d + timedelta(days=1)),
        interval="1d",
        auto_adjust=False if not adjusted else False,
        actions=True,
        progress=False,
    )
    df = _normalize_price_df(df)
    if df is None or df.empty:
        return jsonify({"error": "Sin datos para el rango solicitado"}), 404

    df_out = df.reset_index().copy()
    columns_order = [
        "Date",
        "Open",
        "High",
        "Low",
        "Close",
        "Adj Close",
        "Volume",
        "Dividends",
        "Stock Splits",
    ]
    for column in columns_order:
        if column not in df_out.columns:
            df_out[column] = None
    df_out = df_out[columns_order]
    df_out = df_out.sort_values("Date")

    buffer = io.StringIO()
    df_out.to_csv(buffer, index=False)
    filename = f"{t}_{start_d}_{end_d}{'_adj' if adjusted else ''}.csv"
    return Response(
        buffer.getvalue(),
        headers={
            "Content-Disposition": f'attachment; filename="{filename}"',
            "Content-Type": "text/csv; charset=utf-8",
        },
        status=200,
    )
