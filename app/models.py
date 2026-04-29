from datetime import datetime

from peewee import AutoField, BooleanField, CharField, DateTimeField, ForeignKeyField, IntegerField, Model, TextField

from .db import db_proxy


class BaseModel(Model):
    class Meta:
        database = db_proxy


class User(BaseModel):
    id = AutoField()
    email = CharField(unique=True, max_length=120, index=True)
    username = CharField(max_length=50, null=True)
    password_hash = CharField(max_length=255)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)


class AnalysisHistory(BaseModel):
    id = AutoField()
    user = ForeignKeyField(User, backref="analysis_entries", on_delete="CASCADE")
    ticker = CharField(max_length=20, index=True)
    payload_json = TextField()
    result_json = TextField()
    created_at = DateTimeField(default=datetime.utcnow, index=True)


class CareerSessionLink(BaseModel):
    id = AutoField()
    user = ForeignKeyField(User, backref="career_sessions", on_delete="CASCADE")
    session_id = CharField(max_length=40, unique=True, index=True)
    player = CharField(max_length=120, null=True)
    difficulty = CharField(max_length=32, null=True)
    period_start = CharField(max_length=10, null=True)
    period_end = CharField(max_length=10, null=True)
    created_at = DateTimeField(default=datetime.utcnow, index=True)
    updated_at = DateTimeField(default=datetime.utcnow, index=True)


class CareerSession(BaseModel):
    id = AutoField()
    user = ForeignKeyField(User, backref="career_session_records", on_delete="CASCADE")
    session_id = CharField(max_length=40, unique=True, index=True)
    status = CharField(max_length=24, default="active")
    display_name = CharField(max_length=120, null=True)
    period_start = CharField(max_length=10, null=True)
    period_end = CharField(max_length=10, null=True)
    current_turn = IntegerField(default=1)
    total_turns = IntegerField(default=0)
    latest_snapshot_json = TextField()
    metadata_json = TextField(null=True)
    created_at = DateTimeField(default=datetime.utcnow, index=True)
    updated_at = DateTimeField(default=datetime.utcnow, index=True)


class CareerTurn(BaseModel):
    id = AutoField()
    career_session = ForeignKeyField(CareerSession, backref="turns", on_delete="CASCADE")
    turn_index = IntegerField(index=True)
    decision_json = TextField()
    snapshot_json = TextField()
    result_json = TextField(null=True)
    created_at = DateTimeField(default=datetime.utcnow, index=True)
    updated_at = DateTimeField(default=datetime.utcnow, index=True)

    class Meta:
        indexes = ((('career_session', 'turn_index'), True),)


class ReadinessQuizResult(BaseModel):
    id = AutoField()
    user = ForeignKeyField(User, backref="readiness_results", on_delete="CASCADE", unique=True)
    passed = BooleanField(default=False)
    score = IntegerField(default=0)
    total_questions = IntegerField(default=0)
    passed_at = DateTimeField(null=True)
    answers_json = TextField(null=True)
    created_at = DateTimeField(default=datetime.utcnow, index=True)
    updated_at = DateTimeField(default=datetime.utcnow, index=True)
