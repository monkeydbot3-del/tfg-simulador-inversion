from werkzeug.security import check_password_hash, generate_password_hash

from app.models import User


def get_user_by_id(user_id):
    if not user_id:
        return None
    return User.get_or_none(User.id == user_id)


def get_user_by_email(email: str):
    if not email:
        return None
    return User.get_or_none(User.email == email.strip().lower())


def create_user(email: str, password: str, username: str | None = None):
    normalized_email = (email or "").strip().lower()
    password_hash = generate_password_hash(password)
    normalized_username = (username or "").strip() or None
    return User.create(
        email=normalized_email,
        username=normalized_username,
        password_hash=password_hash,
    )


def authenticate_user(email: str, password: str):
    user = get_user_by_email(email)
    if not user or not user.is_active:
        return None
    if not check_password_hash(user.password_hash, password or ""):
        return None
    return user
