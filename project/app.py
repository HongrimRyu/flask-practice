from flask import Flask, render_template
from flask import Blueprint


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return render_template('base.html', name='Vince')

    return app
