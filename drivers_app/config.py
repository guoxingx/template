# coding: utf-8

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ittaidaregaiyashitekurerudarou'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    WTF_CSRF_ENABLED = False

    SQLALCHEMY_DATABASE_URI = 'mysql://drivers:1234@0.0.0.0:3306/drivers?charset=utf8mb4'
    REDIS_URL = 'redis://@0.0.0.0:6379/0'


class TestConfig(Config):
    DEBUG = True
    FLASK_DEBUG = 1

    SQLALCHEMY_DATABASE_URI = 'mysql://drivers:1234@0.0.0.0:3306/drivers?charset=utf8mb4'
    REDIS_URL = 'redis://@0.0.0.0:6379/0'


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_DEBUG = 1

    SQLALCHEMY_DATABASE_URI = 'mysql://drivers:1234@mysql_conn/drivers?charset=utf8mb4'
    REDIS_URL = 'redis://@redis_conn/0'


config = {
    'test': TestConfig,
    'dev': DevelopmentConfig,
}
