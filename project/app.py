from flask import Flask, render_template
from flask import Blueprint

from config import config_by_name
from flask_sqlalchemy import SQLAlchemy


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    db = SQLAlchemy(app)
    from .views import base
    app.register_blueprint(base.bp)

    return app
