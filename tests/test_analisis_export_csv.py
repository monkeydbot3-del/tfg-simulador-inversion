import csv
import io

# --- Helpers -----------------------------------------------------------


def _client():
    from app import create_app

    app = create_app()
    app.config.update(TESTING=True)
    client = app.test_client()
    client.post("/continuar-invitado")
    return client


def _csv_to_rows(data: bytes):
    return list(csv.reader(io.StringIO(data.decode("utf-8-sig"))))


BASE_PAYLOAD = {
    "ticker": "MSFT",
    "importe_inicial": 1000,
    "horizonte_anios": 2,
    "supuestos": {
        "crecimiento_anual_pct": 5,
        "margen_seguridad_pct": 10,
        "roe_pct": 10,
        "deuda_sobre_activos_pct": 30,
    },
    "justificacion": "Empresa sólida con buenos fundamentales y baja deuda.",
    "modo": "SIN_DCA",
}


# --- Tests -------------------------------------------------------------


def test_csv_basico_descarga_y_cabeceras(tmp_path, monkeypatch):
    """
    Verifica que /analisis.csv devuelve un CSV válido,
    con las cabeceras esperadas (y tolera columnas bt_* adicionales).
    """
    from app import routes

    fake = tmp_path / "analisis.json"
    monkeypatch.setattr(routes, "ANALISIS_PATH", fake)
    c = _client()

    # Generar un par de filas de ejemplo
    for t in ["MSFT", "AAPL"]:
        p = dict(BASE_PAYLOAD, ticker=t)
        assert c.post("/analisis", json=p).status_code == 200

    r = c.get("/analisis.csv")
    assert r.status_code == 403
    assert "exportar historial" in r.get_json()["error"].lower()


def test_csv_vacio(tmp_path, monkeypatch):
    """
    Si no hay registros, el CSV debe contener solo la cabecera.
    """
    from app import routes

    fake = tmp_path / "analisis.json"
    monkeypatch.setattr(routes, "ANALISIS_PATH", fake)
    c = _client()

    r = c.get("/analisis.csv")
    assert r.status_code == 403
    assert "exportar historial" in r.get_json()["error"].lower()
