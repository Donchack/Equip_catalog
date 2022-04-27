import os


app_dir = os.path.abspath(os.path.dirname(__file__))
DB_URI = {
    'mysql_uri':'mysql+pymysql://root:P0rt0k#1@localhost/equip_catalog',
    'postgre_uri':'postgresql://postgres:P0rt0k#1@localhost:5432/equip_catalog'
}

class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'A SECRET KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
            'DEVELOPMENT_DATABASE_URI',
            DB_URI['mysql_uri']
    )


class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
            'TESTING_DATABASE_URI',
			DB_URI['postgre_uri']
    )


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
            'PRODUCTION_DATABASE_URI',
	        DB_URI['postgre_uri']
    )