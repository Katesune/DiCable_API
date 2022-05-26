from flask import Flask, request, render_template, redirect, Blueprint
from flask_login import current_user, login_user, logout_user
from src.blueprints.db.models import login, UserModel, db
from flask import session
from src.blueprints.data import theme

login = Blueprint(name="login", import_name=__name__)

@login.route('/login', methods = ['POST', 'GET'])
 # Маршрут аутентификации пользователя
def auth():
    session.permanent = True
    if current_user.is_authenticated:
        return redirect('/api/data')
    
    if request.method == 'POST':
        email = request.form['email']
        user = UserModel.query.filter_by(email = email).first()
        if user is not None and user.check_password(request.form['password']) and user.remove!=1:
            login_user(user)
            return redirect('/api/data')
        elif user is None or user.remove==1:
            return render_template('login.php', message='Account does not exist or has been deleted', theme=theme)
        elif not user.check_password(request.form['password']):
            # user.set_password(request.form['password'])
            return render_template('login.php', message='Data entered incorrectly', theme=theme)

    return render_template('login.php', message='Enter your login information', theme=theme)

@login.route('/admin', methods=['POST', 'GET'])
 # Админка - достпуна лдя пользователей с типом Admin,
  # В админке можно добавить новых пользователей, 
  # удалить пользователя или восстановить, изменить данные пользователя
def register():

    if current_user.is_authenticated:
        if current_user.type == "admin":
            admins = UserModel.query.filter_by(type = "admin").order_by(UserModel.remove)
            employees = UserModel.query.filter_by(type = "employee").order_by(UserModel.remove)

            if request.method == 'POST':

                if 'remove' in request.form:
                    id = request.form['remove']
                    user = UserModel.query.filter_by(id=id).first()
                    user.remove = 1
                    db.session.commit()
                    return render_template('register.php', admins = admins, employees = employees, theme=theme)

                if 'recover' in request.form:
                    id = request.form['recover']
                    user = UserModel.query.filter_by(id=id).first()
                    user.remove = 0
                    db.session.commit()
                    return render_template('register.php', admins = admins, employees = employees, theme=theme)

                email = request.form['email']
                username = request.form['username']
                type = request.form['type']

                if 'change' in request.form:
                    id = request.form['change']
                    user = UserModel.query.filter_by(id=id).first()
                    user.email = email
                    user.username = username
                    user.type = type
                    db.session.commit()
                    return render_template('register.php', admins = admins, employees = employees, theme=theme)

                password = request.form['password']

                if UserModel.query.filter_by(email=email).first():
                    return render_template('register.php', message='This email is already in the system', admins = admins, employees = employees, theme=theme)
            
                user = UserModel(email=email, username=username, type=type)
                user.set_password(password)

                db.session.add(user)
                db.session.commit()
                return render_template('register.php', message="New user added successfully", admins = admins, employees = employees, theme=theme)
            return render_template('register.php', message="Create a new user", admins = admins, employees = employees, theme=theme)
        else:
            return redirect('/api/data')
        return render_template('register.php', message="Create a new user", theme=theme)
    else:
        return redirect('/api/data')

@login.route('/account', methods=['POST', 'GET'])
#Точка для изменения данных аккаунта
def user_account():
    if current_user.is_authenticated:
        if request.method == 'POST':
            if 'email' in request.form:
                current_user.email = request.form['email']
            if 'username' in request.form:
                current_user.username = request.form['username']
            if 'password' in request.form and not current_user.check_password(request.form['password']):
                current_user.set_password(request.form['password']) 
            if 'type' in request.form:
                current_user.type = request.form['type']
            db.session.commit()
            return render_template('account.php', account_message="Data changed successfully", theme=theme)
        else: 
            return render_template('account.php', account_message="Change your data", theme=theme)
    else:
        return redirect('/auth/login')

@login.route('/logout')
 # Маршрут для выхода из аккаунта
def logout():
    logout_user()
    return redirect('/auth/login')

@login.route('/theme')
 # Кнопка смены темы
def change_theme():
    theme.change_mode()
    return '<script>document.location.href = document.referrer</script>'