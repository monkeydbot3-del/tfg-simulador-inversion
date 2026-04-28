from __future__ import annotations

import json
from datetime import datetime
from typing import Any

from app.models import CareerSession, CareerSessionLink, CareerTurn


def _json_dumps(payload: Any) -> str:
    return json.dumps(payload or {}, ensure_ascii=False)


def _json_loads(payload: str | None, fallback: Any = None) -> Any:
    if not payload:
        return fallback
    try:
        return json.loads(payload)
    except (TypeError, ValueError, json.JSONDecodeError):
        return fallback


def _is_valid_session_payload(payload: Any) -> bool:
    if not isinstance(payload, dict):
        return False
    session_id = str(payload.get("session_id") or "").strip()
    period = payload.get("period") or {}
    turns = payload.get("turns") or []
    return bool(session_id and isinstance(period, dict) and isinstance(turns, list))


def save_career_session_for_user(user_id, session_id, session_payload):
    session_payload = session_payload or {}
    period = session_payload.get("period") or {}
    defaults = {
        "player": (session_payload.get("player") or "").strip() or None,
        "difficulty": (session_payload.get("difficulty") or "").strip() or None,
        "period_start": period.get("start"),
        "period_end": period.get("end"),
        "updated_at": datetime.utcnow(),
    }
    link, created = CareerSessionLink.get_or_create(
        session_id=session_id,
        defaults={
            "user": user_id,
            "created_at": datetime.utcnow(),
            **defaults,
        },
    )
    if not created:
        link.user = user_id
        link.player = defaults["player"]
        link.difficulty = defaults["difficulty"]
        link.period_start = defaults["period_start"]
        link.period_end = defaults["period_end"]
        link.updated_at = defaults["updated_at"]
        link.save()
    return link


def get_latest_career_session_for_user(user_id):
    return (
        CareerSessionLink.select()
        .where(CareerSessionLink.user == user_id)
        .order_by(CareerSessionLink.updated_at.desc(), CareerSessionLink.created_at.desc())
        .first()
    )


def list_career_sessions_for_user(user_id, limit=12):
    query = (
        CareerSessionLink.select()
        .where(CareerSessionLink.user == user_id)
        .order_by(CareerSessionLink.updated_at.desc(), CareerSessionLink.created_at.desc())
    )
    if limit:
        query = query.limit(limit)
    return list(query)


def upsert_career_session_state(user_id: int, session_payload: dict[str, Any]) -> CareerSession:
    session_payload = session_payload or {}
    if not _is_valid_session_payload(session_payload):
        raise ValueError("La sesión de carrera no tiene un payload válido para persistencia.")
    session_id = str(session_payload.get("session_id") or "").strip()
    if not session_id:
        raise ValueError("session_id es obligatorio para persistir la sesión de carrera.")

    period = session_payload.get("period") or {}
    player = (session_payload.get("player") or "").strip() or None
    difficulty = (session_payload.get("difficulty") or "").strip() or None
    closed = bool(session_payload.get("closed"))
    status = "closed" if closed else "active"
    completed_turns = session_payload.get("completed_turns") or []
    current_turn = len(completed_turns) + 1
    total_turns = int(session_payload.get("turns_total") or session_payload.get("total_turns") or 0)
    metadata = {
        "period": period,
        "capital_initial": session_payload.get("capital_initial"),
        "capital_current": session_payload.get("capital_current"),
        "cum_return": session_payload.get("cum_return"),
        "closed": closed,
        "difficulty": difficulty,
        "player": player,
    }

    defaults = {
        "user": user_id,
        "display_name": player,
        "status": status,
        "current_turn": current_turn,
        "total_turns": total_turns,
        "period_start": period.get("start"),
        "period_end": period.get("end"),
        "latest_snapshot_json": _json_dumps(session_payload),
        "metadata_json": _json_dumps(metadata),
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }

    record, created = CareerSession.get_or_create(session_id=session_id, defaults=defaults)
    if not created:
        record.user = user_id
        record.display_name = player
        record.status = status
        record.current_turn = current_turn
        record.total_turns = total_turns
        record.period_start = period.get("start")
        record.period_end = period.get("end")
        record.latest_snapshot_json = _json_dumps(session_payload)
        record.metadata_json = _json_dumps(metadata)
        record.updated_at = datetime.utcnow()
        record.save()

    save_career_session_for_user(user_id, session_id, session_payload)
    return record


def save_career_turn_state(
    user_id: int,
    session_payload: dict[str, Any],
    turn_index: int,
    decision_payload: dict[str, Any] | None = None,
    snapshot_payload: dict[str, Any] | None = None,
    result_payload: dict[str, Any] | None = None,
) -> CareerTurn:
    record = upsert_career_session_state(user_id, session_payload)
    defaults = {
        "decision_json": _json_dumps(decision_payload or {}),
        "snapshot_json": _json_dumps(snapshot_payload or {}),
        "result_json": _json_dumps(result_payload or {}),
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }
    turn, created = CareerTurn.get_or_create(
        career_session=record,
        turn_index=turn_index,
        defaults=defaults,
    )
    if not created:
        turn.decision_json = defaults["decision_json"]
        turn.snapshot_json = defaults["snapshot_json"]
        turn.result_json = defaults["result_json"]
        turn.updated_at = datetime.utcnow()
        turn.save()
    return turn


def get_persisted_career_session_for_user(user_id: int, session_id: str) -> CareerSession | None:
    return (
        CareerSession.select()
        .where((CareerSession.user == user_id) & (CareerSession.session_id == session_id))
        .first()
    )


def get_latest_persisted_career_session_for_user(user_id: int) -> CareerSession | None:
    return (
        CareerSession.select()
        .where(CareerSession.user == user_id)
        .order_by(CareerSession.updated_at.desc(), CareerSession.created_at.desc())
        .first()
    )


def deserialize_career_session(record: CareerSession | None) -> dict[str, Any] | None:
    if not record:
        return None
    payload = _json_loads(record.latest_snapshot_json, fallback=None)
    if not _is_valid_session_payload(payload):
        return None
    return payload


def list_persisted_career_turns_for_user(user_id: int, session_id: str) -> list[dict[str, Any]]:
    session_record = get_persisted_career_session_for_user(user_id, session_id)
    if not session_record:
        return []
    query = (
        CareerTurn.select()
        .where(CareerTurn.career_session == session_record)
        .order_by(CareerTurn.turn_index.asc(), CareerTurn.created_at.asc())
    )
    items: list[dict[str, Any]] = []
    for item in query:
        items.append(
            {
                "turn_index": item.turn_index,
                "decision": _json_loads(item.decision_json, fallback={}),
                "snapshot": _json_loads(item.snapshot_json, fallback={}),
                "result": _json_loads(item.result_json, fallback={}),
                "created_at": item.created_at.isoformat() + "Z",
                "updated_at": item.updated_at.isoformat() + "Z",
            }
        )
    return items
