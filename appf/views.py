from appf import app
from flask_login import current_user

from .models import Equip, Type_eq, Manufacturer, db

@app.route('/')
def index():
    if current_user.is_authenticated:
        name_user = f', {current_user.user_name}'
    else:
        name_user = ''
    return f'Привет{name_user}! Это приложение "Каталог оборудования"'
    