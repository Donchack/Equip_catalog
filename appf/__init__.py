from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from flask_script import Manager, Command, Shell
import os, config

# создание экземпляра приложения
app = Flask(__name__)
app.config.from_object(
        os.environ.get('FLASK_ENV')
        or config.DevelopmentConfig
)
# инициализирует расширения
db = SQLAlchemy(app)
# migrate = Migrate(app, db)
from .main import main as main_blp
app.register_blueprint(main_blp, url_prefix='')
