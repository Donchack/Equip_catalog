import os 
from flask import Flask
# from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from flask_script import Manager, Command, Shell
import config


# создание экземпляра приложения
app = Flask(__name__)
app.config.from_object(
        os.environ.get('FLASK_ENV')
        or config.DevelopmentConfig
)
# инициализирует расширения
db = SQLAlchemy(app)
# migrate = Migrate(app, db)

import appf.models
from .admin import main as main_blp, login_manager

import appf.views
login_manager.init_app(app)

app.register_blueprint(main_blp, url_prefix='')


