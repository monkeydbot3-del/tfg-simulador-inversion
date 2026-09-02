from app import create_app
from app.models import User
from app.services.auth_service import create_user


def test_index_served():
    app = create_app()
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 302
    assert "/login" in res.headers.get("Location", "")


def test_guest_navbar_shows_guest_state_and_login():
    app = create_app()
    client = app.test_client()

    with client.session_transaction() as flask_session:
        flask_session["guest"] = True

    res = client.get("/aprende")
    html = res.get_data(as_text=True)

    assert res.status_code == 200
    assert "Modo invitado" in html
    assert "Sin historial persistente" in html
    assert "Iniciar sesión" in html


def test_guest_can_open_login_form_from_guest_state():
    app = create_app()
    client = app.test_client()

    with client.session_transaction() as flask_session:
        flask_session["guest"] = True

    res = client.get("/login", follow_redirects=False)
    assert res.status_code == 200
    html = res.get_data(as_text=True)
    assert "<h1>Iniciar sesión</h1>" in html

    with client.session_transaction() as flask_session:
        assert flask_session.get("guest") is None


def test_authenticated_navbar_hides_guest_state_after_login_from_guest_session():
    app = create_app()

    with app.app_context():
        user = User.get_or_none(User.email == "navbar@example.com")
        if not user:
            user = create_user(
                email="navbar@example.com",
                password="supersecreto",
                username="NavUser",
            )

    client = app.test_client()

    with client.session_transaction() as flask_session:
        flask_session["guest"] = True
        flask_session["readiness_guest"] = {"passed": False, "score": 4}

    login = client.post(
        "/login",
        data={"email": "navbar@example.com", "password": "supersecreto"},
        follow_redirects=True,
    )
    html = login.get_data(as_text=True)

    assert login.status_code == 200
    assert "Modo invitado" not in html
    assert "Sin historial persistente" not in html
    assert ">Iniciar sesión<" not in html
    assert "Cerrar sesión" in html
    assert "NavUser" in html or "navbar@example.com" in html

    with client.session_transaction() as flask_session:
        assert flask_session.get("user_id") is not None
        assert flask_session.get("guest") is None


def test_guest_can_open_register_form_from_guest_state():
    app = create_app()
    client = app.test_client()

    with client.session_transaction() as flask_session:
        flask_session["guest"] = True

    res = client.get("/registro", follow_redirects=False)
    assert res.status_code == 200
    html = res.get_data(as_text=True)
    assert "<h1>Crear cuenta</h1>" in html

    with client.session_transaction() as flask_session:
        assert flask_session.get("guest") is None


def test_logout_clears_session_state():
    app = create_app()

    with app.app_context():
        user = User.get_or_none(User.email == "logout@example.com")
        if not user:
            user = create_user(
                email="logout@example.com",
                password="supersecreto",
                username="LogoutUser",
            )

    client = app.test_client()

    with client.session_transaction() as flask_session:
        flask_session["user_id"] = user.id
        flask_session["guest"] = True

    res = client.post("/logout", follow_redirects=False)
    assert res.status_code == 302

    with client.session_transaction() as flask_session:
        assert flask_session.get("user_id") is None
        assert flask_session.get("guest") is None


def test_authenticated_navbar_hides_anonymous_actions_on_internal_pages():
    app = create_app()

    with app.app_context():
        user = User.get_or_none(User.email == "internal-pages@example.com")
        if not user:
            user = create_user(
                email="internal-pages@example.com",
                password="supersecreto",
                username="InternalUser",
            )

    client = app.test_client()
    login = client.post(
        "/login",
        data={"email": "internal-pages@example.com", "password": "supersecreto"},
        follow_redirects=False,
    )
    assert login.status_code == 302

    for path in ["/nuevo-analisis", "/aprende", "/modo-carrera", "/modo-horizonte"]:
        res = client.get(path)
        html = res.get_data(as_text=True)
        assert res.status_code == 200, path
        assert "Modo invitado" not in html, path
        assert "Sin historial persistente" not in html, path
        assert ">Iniciar sesión<" not in html, path
        assert ">Crear cuenta<" not in html, path
        assert "Cerrar sesión" in html, path
