from flask import Flask, render_template
from flask import Blueprint

from config import config_by_name


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    from .views import base
    app.register_blueprint(base.bp)

    @app.route('/')
    def hello():
        return render_template('base.html', name='Vince')

    return app
