import os

class BaseConfig():
    TESTING = False
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') # use os.random(string) or something like that
    SESSION_TYPE = 'filesystem'
    DB_NAME = 'production-db'
    SESSION_COOKIE_SECURE = True # cookies are only send if https

class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True
    DB_NAME = 'development-db'


class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
    DEBUG = False
    SESSION_COOKIE_SECURE = False


class TestConfig(BaseConfig):
    FLASK_ENV = 'development'
    TESTING = True
    SESSION_COOKIE_SECURE = False
