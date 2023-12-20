import os


class BaseConfig():
    TESTING = False
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_TYPE = 'filesystem'
    SESSION_COOKIE_SECURE = True # cookies are only send if https

class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/simradar_dev' # test DB in local server

class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://root:mjhBmBi3mPCaONfaMkql27bCA6glm3je@dpg-cm12r4en7f5s73e3numg-a.oregon-postgres.render.com/simradar_prod'
    SESSION_COOKIE_SECURE = False

class TestConfig(BaseConfig):
    FLASK_ENV = 'testing'
    TESTING = True
    SESSION_COOKIE_SECURE = False