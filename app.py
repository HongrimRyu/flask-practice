import os

from project.app import create_app
env = os.environ.get('FLASK_ENV', 'development')
application = create_app(env)
