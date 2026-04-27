from datetime import datetime

from app.models import CareerSessionLink


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
