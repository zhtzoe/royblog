import os

class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'royblog is awesome'

class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/royblog?charset=utf8'

class TestConfig(BaseConfig):
    pass

class ProdConfig(BaseConfig):
    pass

configs = {
    'dev':DevConfig,
    'test':TestConfig,
    'prd':ProdConfig
}