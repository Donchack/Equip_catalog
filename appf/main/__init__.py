from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import Login_form

_users = {'Admin':'1234', 'User1':'4321'}
main = Blueprint('main', __name__, template_folder='templates') 
# static_folder='../static'
@main.route('/', methods=['GET', 'POST'])
def login():
    form = Login_form()
    if form.validate_on_submit():
        name = form.user_login.data
        psw = form.user_psw.data
        if name in _users and _users[name] == psw:
            flash(f'{name}, вы вбили правильный пароль!!!')
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
def profile(user):
    message = f'Вы зашли как пользователь {user}'
    return render_template('profile.html', message=message)
