
from celery import Celery


class TasksLoader(object):

    def init_app(self, flask_app):
        pass

    def register(self, func):
        setattr(self, func.__name__, func)


celery = Celery()


def init_app(self, flask_app):
    celery.main = flask_app.name
    celery.broker = flask_app.config['REDIS_URL']
    celery.conf.update(flask_app.config)


celery.init_app = init_app
