
from flask import Flask
from flask_cors import CORS

from config import config
from .db import db
from .utils import populate_config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    populate_config(config[config_name])

    db.init_app(app)
    CORS(app, max_age=86400)

    return app
