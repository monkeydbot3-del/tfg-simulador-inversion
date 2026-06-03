import json
from datetime import datetime

from app.models import AnalysisHistory


def save_analysis_for_user(user_id, ticker, payload, result):
    return AnalysisHistory.create(
        user=user_id,
        ticker=(ticker or "").strip().upper(),
        payload_json=json.dumps(payload, ensure_ascii=False),
        result_json=json.dumps(result, ensure_ascii=False),
        created_at=datetime.utcnow(),
    )


def _entry_to_dict(entry):
    payload = json.loads(entry.payload_json or "{}")
    result = json.loads(entry.result_json or "{}")
    registro = {
        "id": str(entry.id),
        "timestamp": entry.created_at.isoformat() + "Z",
        "ticker": entry.ticker,
    }
    if isinstance(payload, dict):
        registro.update(payload)
    if isinstance(result, dict):
        registro.update(result)
    return registro


def list_analysis_for_user(user_id, ticker=None, desde=None, hasta=None):
    query = AnalysisHistory.select().where(AnalysisHistory.user == user_id)
    if ticker:
        query = query.where(AnalysisHistory.ticker == (ticker or "").strip().upper())
    if desde:
        query = query.where(AnalysisHistory.created_at >= datetime.fromisoformat(desde))
    if hasta:
        query = query.where(AnalysisHistory.created_at < datetime.fromisoformat(hasta))
    query = query.order_by(AnalysisHistory.created_at.desc())
    return [_entry_to_dict(entry) for entry in query]
