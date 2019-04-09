from flask import Flask
from royblog.config import configs

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    pass

def register_blueprints(app):
    from .handlers import front
    app.register_blueprint(front)
