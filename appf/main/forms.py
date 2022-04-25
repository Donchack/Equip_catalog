from email.policy import default
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length

class Login_form(FlaskForm):
    user_login = StringField(
            'Логин', 
            validators=[
                    DataRequired(message='Логин не может быть пустым'),
                    Length(min=3, max=20, 
                           message='Длина логина от 3 до 20 символов')
            ]
    )
    user_psw = PasswordField(
            'Пароль',
            validators=[
                    DataRequired(message='Пароль не может быть пустым'),
                    Length(min=3, max=20, 
                           message='Длина пароля от 3 до 20 символов')
            ]

    )
    rememder = BooleanField('Запомнить', default=False)
    submit = SubmitField('Войти')

