import os

from peewee import DatabaseProxy
from playhouse.db_url import connect


db_proxy = DatabaseProxy()


def init_db():
    database_url = os.environ.get("DATABASE_URL")
    if not database_url:
        raise RuntimeError("DATABASE_URL no está configurada.")
    database = connect(database_url)
    db_proxy.initialize(database)
    return database


def connect_db():
    if db_proxy.obj is not None and db_proxy.is_closed():
        db_proxy.connect(reuse_if_open=True)


def close_db():
    if db_proxy.obj is not None and not db_proxy.is_closed():
        db_proxy.close()
