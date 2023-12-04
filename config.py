import os

class BaseConfig():
    TESTING = False
    DEBUG = False
    SECRET_KEY = '30ce06bd5a0d6089a26e0e84e933947f'
    SESSION_TYPE = 'filesystem'
    SESSION_COOKIE_SECURE = True # cookies are only send if https

class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True

class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
    DEBUG = False
    SESSION_COOKIE_SECURE = False

class TestConfig(BaseConfig):
    FLASK_ENV = 'testing'
    TESTING = True
    SESSION_COOKIE_SECURE = False