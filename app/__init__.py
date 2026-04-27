import os

import matplotlib

# Force a headless backend so Matplotlib never opens GUI windows on the server.
matplotlib.use("Agg")

from flask import Flask

from .auth import auth_bp
from .career import career_bp
from .db import close_db, connect_db, init_db
from .models import AnalysisHistory, CareerSessionLink, User
from .routes import bp as main_bp


def create_app() -> Flask:
    secret_key = os.environ.get("SECRET_KEY")
    if not secret_key:
        raise RuntimeError("SECRET_KEY no está configurada.")

    app = Flask(__name__)
    app.config["SECRET_KEY"] = secret_key
    database = init_db()

    @app.before_request
    def _before_request():
        connect_db()

    @app.teardown_appcontext
    def _teardown_db(_exc):
        close_db()

    with database:
        database.create_tables([User, AnalysisHistory, CareerSessionLink], safe=True)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(career_bp)
    return app
