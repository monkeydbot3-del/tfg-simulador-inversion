from datetime import datetime

from peewee import AutoField, BooleanField, CharField, DateTimeField, ForeignKeyField, Model, TextField

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
