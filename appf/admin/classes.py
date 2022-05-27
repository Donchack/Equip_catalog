import string
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):
    def __init__(self, id:int, user_name:str, password:str):
        self.id = id
        self.user_name = user_name
        self.psw_hash = generate_password_hash(password)
    
    def check_password(self, password: str) -> bool:
        return check_password_hash(self.psw_hash, password)

    def get_id(self) -> int:
        return self.id

    def __repr__(self) -> str:
        return f'{self.id}:{self.user_name}'