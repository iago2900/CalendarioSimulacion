import os

class BaseConfig():
    TESTING = False
    DEBUG = False
    SESSION_TYPE = 'filesystem'
    SESSION_COOKIE_SECURE = True # cookies are only send if https

class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True
    SECRET_KEY = 'some_test_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/simradar_dev' # test DB in local server

class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL')
    SESSION_COOKIE_SECURE = False