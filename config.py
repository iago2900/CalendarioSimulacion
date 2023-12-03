import os

class BaseConfig():
    TESTING = False
    DEBUG = False
    SECRET_KEY = os.urandom(16).hex()
    SESSION_TYPE = 'filesystem'
    SESSION_COOKIE_SECURE = True # cookies are only send if https

class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True
    DB_NAME = 'development-db'


class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
    DEBUG = False
    SESSION_COOKIE_SECURE = False
    DB_NAME = 'production-db'


class TestConfig(BaseConfig):
    FLASK_ENV = 'testing'
    TESTING = True
    SESSION_COOKIE_SECURE = False
    DB_NAME = 'test-db'