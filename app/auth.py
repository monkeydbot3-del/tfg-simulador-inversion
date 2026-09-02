from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from .services.auth_service import authenticate_user, create_user, get_user_by_email


auth_bp = Blueprint("auth", __name__)


@auth_bp.get("/registro")
def register_page():
    if session.get("user_id"):
        return redirect(url_for("main.home"))
    if session.get("guest"):
        session.pop("guest", None)
        session.modified = True
    return render_template("register.html", active="register", nav_mode="practice")


@auth_bp.post("/registro")
def register_submit():
    email = (request.form.get("email") or "").strip().lower()
    username = (request.form.get("username") or "").strip()
    password = request.form.get("password") or ""
    password_confirm = request.form.get("password_confirm") or ""

    if not email or "@" not in email:
        flash("Introduce un correo válido.", "error")
        return redirect(url_for("auth.register_page"))
    if len(password) < 8:
        flash("La contraseña debe tener al menos 8 caracteres.", "error")
        return redirect(url_for("auth.register_page"))
    if password != password_confirm:
        flash("Las contraseñas no coinciden.", "error")
        return redirect(url_for("auth.register_page"))
    if get_user_by_email(email):
        flash("Ya existe una cuenta con ese correo.", "error")
        return redirect(url_for("auth.register_page"))

    user = create_user(email=email, password=password, username=username or None)
    session.clear()
    session["user_id"] = user.id
    flash("Cuenta creada correctamente.", "success")
    return redirect(url_for("main.historial_page"))


@auth_bp.get("/login")
def login_page():
    if session.get("user_id"):
        return redirect(url_for("main.home"))
    if session.get("guest"):
        session.pop("guest", None)
        session.modified = True
    return render_template("login.html", active="login", nav_mode="practice")


@auth_bp.post("/login")
def login_submit():
    email = (request.form.get("email") or "").strip().lower()
    password = request.form.get("password") or ""
    user = authenticate_user(email, password)
    if not user:
        flash("Credenciales no válidas.", "error")
        return redirect(url_for("auth.login_page"))

    previous_guest_readiness = session.get("readiness_guest")
    session.clear()
    session["user_id"] = user.id
    if previous_guest_readiness and not previous_guest_readiness.get("passed"):
        session["readiness_guest_last_attempt"] = previous_guest_readiness
    flash("Has iniciado sesión correctamente.", "success")
    return redirect(url_for("main.home"))


@auth_bp.post("/continuar-invitado")
def continue_as_guest():
    session.clear()
    session["guest"] = True
    flash("Has entrado en modo invitado. Tus análisis no se guardarán.", "success")
    return redirect(url_for("main.home"))


@auth_bp.post("/logout")
def logout_submit():
    session.clear()
    flash("Has cerrado sesión.", "success")
    return redirect(url_for("main.home"))
