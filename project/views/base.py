from flask import app, Blueprint

bp = Blueprint('base', __name__, url_prefix='/base')


@bp.route('/')
def auth_base_view():
    return 'auth'