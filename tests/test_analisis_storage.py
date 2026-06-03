from app import create_app


def _client():
    app = create_app()
    client = app.test_client()
    client.post("/continuar-invitado")
    return client


def _payload_base():
    return {
        "ticker": "MSFT",
        "importe_inicial": 500,
        "horizonte_anios": 10,
        "supuestos": {
            "crecimiento_anual_pct": 8,
            "margen_seguridad_pct": 20,
            "roe_pct": 18,
            "deuda_sobre_activos_pct": 25,
        },
        "justificacion": "Caso de prueba persistencia.",
    }


def test_post_analisis_guarda_en_historial_y_get_lista():
    c = _client()

    # 1) POST crea un análisis y lo devuelve con puntuación/resumen
    res = c.post("/analisis", json=_payload_base())
    assert res.status_code == 200
    data = res.get_json()
    assert data["valido"] is True
    assert isinstance(data["puntuacion"], int)

    # 2) GET /analisis devuelve una lista con al menos 1 elemento
    res2 = c.get("/analisis")
    assert res2.status_code == 403
    data2 = res2.get_json()
    assert "historial" in data2["error"].lower()


def test_get_analisis_vacio_no_revienta(tmp_path, monkeypatch):
    # Simulamos que el fichero no existe aún
    from app import routes

    fake_path = tmp_path / "analisis.json"
    monkeypatch.setattr(routes, "ANALISIS_PATH", fake_path)

    c = _client()
    res = c.get("/analisis")
    assert res.status_code == 403
    assert "historial" in res.get_json()["error"].lower()
