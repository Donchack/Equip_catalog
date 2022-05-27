from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from flask_login import LoginManager, login_user, login_required, current_user

from .forms import Login_form
from .classes import User


users = []
users.append(User(1, 'Admin', '1234'))
users.append(User(2, 'AdUser1min', '4321'))

main = Blueprint('main', __name__, template_folder='templates')
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    for usr in users:
        if user_id == usr.get_id():
            return usr

# static_folder='../static'
@main.route('login/', methods=['GET', 'POST'])
def login():
    
    form = Login_form()
    if form.validate_on_submit():
        name = form.user_login.data
        for usr in users:
            if (usr.user_name == name 
                    and usr.check_password(form.user_psw.data)):
                flash(f'{name}, вы вбили правильный пароль!!!')
                login_user(usr)
                print(current_user.get_id())
                return redirect(url_for('.profile', user=name))
        else:
            flash(f'Пользователя {name} не существует или пароль введен неправильно!!!')
            form.user_login.data = ''
    return render_template(
            'login_form.html', 
            message=f'Это приложение "Каталог оборудования"',
            form=form
    )

@main.route('/profile/<user>')
@login_required
def profile(user):
    message = f'Вы зашли как пользователь {user}'
    return render_template('profile.html', message=message)

@main.route('/profile')
@login_required
def profiles():
    if current_user.is_authenticated:
        return redirect(url_for('.profile', user=current_user.user_name))
