from flask import Flask, render_template, request, redirect, flash, g
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from FDataBase import FDataBase
import sqlite3
import os
from UserLogin import UserLogin


DATABASE = '/flsite.db'
DEBUG = True
SECRET_KEY = 'jd ivhde8qyfcjndkvnfknbfghrifojvdn vkdn i efjefjdivhdubhh nicx sdiovhdun jvhsduogvdvb ndijveiohgvd'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))
login_manager = LoginManager(app)


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():

    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():

    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


dbase = None
@app.before_request
def before_request():
    global dbase
    db = get_db()
    dbase = FDataBase(db)


@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return UserLogin().fromDB(user_id, dbase)


@app.teardown_appcontext
def close_db(error):

    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/library')
@login_required
def library():
    return render_template("library.html", menu=dbase.getMenu())


@app.route('/account')
@login_required
def account():
    acc_id = current_user.get_id()
    return render_template("account.html", menu=dbase.getMenu(), acc_id=acc_id)


@app.route('/logout')
def logout():
    logout_user()
    flash("Вы вышли из аккаунта", "success")
    return redirect('/enter')


@app.route('/enter', methods=['GET', 'POST'])
def enter():
    if request.method == "POST":
        user = dbase.getUserByEmail(request.form['email'])
        if user and check_password_hash(user['password'], request.form['password']):
            user_login = UserLogin().create(user)
            login_user(user_login)
            return redirect('/account')

        else:
            flash("Неверная пара email/пароль", "error")

    return render_template("enter.html", menu=dbase.getMenu())


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == "POST":
        if len(request.form['user_email']) > 4 and len(request.form['user_name']) > 4 \
            and len(request.form['user_password']) > 4 and request.form['user_password'] == request.form['second_user_password']:
            hash = generate_password_hash(request.form['user_password'])
            res = dbase.addUser(request.form['user_email'], request.form['user_name'], hash)
            if res:
                flash('Вы зарегистрировались. Теперь необходимо войти', 'success')
                return redirect('/enter')
            else:
                flash('Ошибка при добавлении в БД')
        else:
            flash('Неверно заполнены поля', 'error')
    return render_template("registration.html", menu=dbase.getMenu())


if __name__ == "__main__":
    app.run(port=6060)
