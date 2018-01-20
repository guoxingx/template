# coding: utf-8

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ittaidaregaiyashitekurerudarou'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    WTF_CSRF_ENABLED = False


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_DEBUG = 1

    SQLALCHEMY_DATABASE_URI = 'mysql://temp_user:1234@mysql_conn/gio?charset=utf8mb4'
    REDIS_URL = 'redis://@redis_conn/0'


config = {
    'test': DevelopmentConfig,
    'development': DevelopmentConfig,
}
