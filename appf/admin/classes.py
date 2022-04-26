import string
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


class User(UserMixin):
    def __init__(self, id:int, user_name:str, password:str):
        self.id = id
        self.user_name = user_name
        self.psw_hash = generate_password_hash(password)