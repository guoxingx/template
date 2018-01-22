
from flask import Flask
from flask_cors import CORS

from config import config
from .db import db
from ._celery import TasksLoader
from .utils import populate_config


tasks_loader = TasksLoader()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    populate_config(config[config_name])

    db.init_app(app)
    tasks_loader.init_app(app)
    CORS(app, max_age=86400)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from tasks import grab_carbens
    tasks_loader.register(grab_carbens)

    return app
