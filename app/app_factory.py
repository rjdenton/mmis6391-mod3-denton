from flask import Flask
from .db import get_db_connection


def create_app():

    app = Flask(__name__)

    with app.app_context():
        conn = get_db_connection()

    from .routes import init_routes
    init_routes(app)

    return app