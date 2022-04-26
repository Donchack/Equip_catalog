from appf import app

from .models import Equip, Type_eq, Manufacturer, db

@app.route('/')
def index():
    return 'Ну привет! Это приложение "Каталог оборудования"'