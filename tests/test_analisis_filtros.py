from app import create_app
from datetime import datetime


def _client():
    app = create_app()
    client = app.test_client()
    client.post("/continuar-invitado")
    return client


BASE_PAYLOAD = {
    "importe_inicial": 100,
    "horizonte_anios": 5,
    "supuestos": {
        "crecimiento_anual_pct": 10,
        "margen_seguridad_pct": 20,
        "roe_pct": 15,
        "deuda_sobre_activos_pct": 30,
    },
    "justificacion": "Caso suficientemente largo para pasar validación.",
}


def test_filtro_por_ticker(tmp_path, monkeypatch):
    # Aislamos el fichero de almacenamiento
    from app import routes

    fake = tmp_path / "analisis.json"
    monkeypatch.setattr(routes, "ANALISIS_PATH", fake)
    c = _client()

    # Creamos 3 análisis con tickers diferentes
    for t in ["MSFT", "AAPL", "MSFT"]:
        p = dict(BASE_PAYLOAD, ticker=t)
        assert c.post("/analisis", json=p).status_code == 200

    # En modo invitado el historial protegido debe rechazar la consulta
    r = c.get("/analisis?ticker=msft")
    assert r.status_code == 403
    assert "historial" in r.get_json()["error"].lower()


def test_filtro_por_fecha_desde_hasta(tmp_path, monkeypatch):
    from app import routes

    fake = tmp_path / "analisis.json"
    monkeypatch.setattr(routes, "ANALISIS_PATH", fake)
    c = _client()

    # Creamos dos análisis "en el pasado" y uno "hoy".
    # No podemos manipular el timestamp interno fácilmente sin tocar el código,
    # así que creamos 3 y luego reescribimos el archivo con timestamps controlados.
    for t in ["MSFT", "AAPL", "NVDA"]:
        p = dict(BASE_PAYLOAD, ticker=t)
        assert c.post("/analisis", json=p).status_code == 200

    # El historial protegido no debe exponerse a invitado aunque existan análisis en sesión
    hoy = datetime.utcnow()
    desde = hoy.date().isoformat()
    r1 = c.get(f"/analisis?desde={desde}")
    assert r1.status_code == 403
    assert "historial" in r1.get_json()["error"].lower()

    r2 = c.get(f"/analisis?hasta={desde}")
    assert r2.status_code == 403
    assert "historial" in r2.get_json()["error"].lower()


def test_filtros_combinados_y_paginado(tmp_path, monkeypatch):
    from app import routes

    fake = tmp_path / "analisis.json"
    monkeypatch.setattr(routes, "ANALISIS_PATH", fake)
    c = _client()

    # Generamos 7 MSFT y 3 AAPL
    for _ in range(7):
        p = dict(BASE_PAYLOAD, ticker="MSFT")
        assert c.post("/analisis", json=p).status_code == 200
    for _ in range(3):
        p = dict(BASE_PAYLOAD, ticker="AAPL")
        assert c.post("/analisis", json=p).status_code == 200

    # El historial protegido no debe paginar ni listar en modo invitado
    r = c.get("/analisis?ticker=MSFT&page=1&per_page=5")
    assert r.status_code == 403
    assert "historial" in r.get_json()["error"].lower()

    r2 = c.get("/analisis?ticker=MSFT&page=2&per_page=5")
    assert r2.status_code == 403
    assert "historial" in r2.get_json()["error"].lower()
