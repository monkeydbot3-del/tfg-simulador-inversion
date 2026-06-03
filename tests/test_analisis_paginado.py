from app import create_app


def _client():
    app = create_app()
    client = app.test_client()
    client.post("/continuar-invitado")
    return client


def test_analisis_paginado_lista_y_meta(tmp_path, monkeypatch):
    # Usar fichero temporal para no tocar datos reales
    from app import routes

    fake = tmp_path / "analisis.json"
    monkeypatch.setattr(routes, "ANALISIS_PATH", fake)

    c = _client()
    payload = {
        "ticker": "MSFT",
        "importe_inicial": 100,
        "horizonte_anios": 5,
        "supuestos": {
            "crecimiento_anual_pct": 10,
            "margen_seguridad_pct": 20,
            "roe_pct": 15,
            "deuda_sobre_activos_pct": 30,
        },
        "justificacion": "Caso demo lo bastante largo para pasar validación.",
    }

    # Genera 6 análisis
    for _ in range(6):
        assert c.post("/analisis", json=payload).status_code == 200

    res = c.get("/analisis?page=1&per_page=5")
    assert res.status_code == 403
    assert "historial" in res.get_json()["error"].lower()

    res2 = c.get("/analisis?page=2&per_page=5")
    assert res2.status_code == 403
    assert "historial" in res2.get_json()["error"].lower()
