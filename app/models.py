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
