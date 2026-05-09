from app import create_app


def test_index_served():
    app = create_app()
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 302
    assert "/login" in res.headers.get("Location", "")
