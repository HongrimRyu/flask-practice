from flask import app, Blueprint, render_template

bp = Blueprint('base', __name__, url_prefix='/')


@bp.route('/')
def base_view():
    return render_template('base.html')