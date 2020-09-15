from flask import Flask, render_template
from flask import Blueprint


def create_app():
    app = Flask(__name__)

    from .views import base
    app.register_blueprint(base.bp)

    @app.route('/')
    def hello():
        return render_template('base.html', name='Vince')

    return app
