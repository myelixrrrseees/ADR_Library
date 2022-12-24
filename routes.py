from flask import Flask, render_template, request, redirect, flash, g, make_response, session
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from FDataBase import FDataBase
import datetime
import sqlite3
import os
from UserLogin import UserLogin


DATABASE = '/flsite.db'
DEBUG = True
SECRET_KEY = 'jd ivhde8qyfcjndkvnfknbfghrifojvdn vkdn i efjefjdivhdubhh nicx sdiovhdun jvhsduogvdvb ndijveiohgvd'
MAX_CONTENT_LENGTH = 1024 * 1024

app = Flask(__name__)
app.config.from_object(__name__)
app.permanent_session_lifetime = datetime.timedelta(days=365)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))

login_manager = LoginManager(app)
login_manager.login_view = 'enter'
login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"
login_manager.login_message_category = "success"


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


@app.route('/session_of_book', methods=['GET', 'POST'])
def session_of_book():
    if request.method == 'POST':
        print('Все ок')
        if not session.get('dobav'):
            try:
                session['dobav'] = []
            except:
                print('Не удалось')
        try:
            session['book_image'] = request.form['book_image']
            print('Все вери ок')
        except:
            print('Оу нееет')
    else:
        print('Не ок')

    return render_template('account.html', session=session)


@app.route('/library')
@login_required
def library():
    return render_template("library.html", menu=dbase.getMenuBook())


@app.route('/account')
@login_required
def account():
    acc_id = current_user.get_id()
    return render_template("account.html", menu=dbase.getMenuUser(), acc_id=acc_id)


@app.route('/userava')
@login_required
def userava():
    img = current_user.getAvatar(app)
    if not img:
        return ""

    h = make_response(img)
    h.headers['Content-Type'] = 'image/png'
    return h


@app.route('/upload', methods=["POST", "GET"])
@login_required
def upload():
    if request.method == "POST":
        file = request.files['file']
        if file:
            if current_user.verifyExt(file.filename):
                try:
                    img = file.read()
                    res = dbase.updateUserAvatar(img, current_user.get_id())
                    if not res:
                        flash("Ошибка обновления аватара", "error")
                        return redirect('/account')
                    flash("Аватар обновлен", "success")
                except FileNotFoundError:
                    flash("Ошибка чтения файла 1", "error")
            else:
                flash("Ошибка чтения файла 2", "error")
        else:
            flash("Ошибка чтения файла 3", "error")
    return redirect('/account')


@app.route('/logout')
def logout():
    logout_user()
    flash("Вы вышли из аккаунта", "success")
    return redirect('/enter')


@app.route('/enter', methods=['GET', 'POST'])
def enter():
    if current_user.is_authenticated:
        return redirect('/account')

    if request.method == "POST":
        user = dbase.getUserByEmail(request.form['email'])
        if user and check_password_hash(user['password'], request.form['password']):
            user_login = UserLogin().create(user)
            rm = True if request.form.get('remember_me') else False
            login_user(user_login, remember=rm)
            return redirect(request.args.get("next") or ('/account'))

        else:
            flash("Неверная пара email/пароль", "error")

    return render_template("enter.html", menu=dbase.getMenuUser())


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == "POST":
        if len(request.form['user_email']) > 4 and len(request.form['user_name']) > 4 \
            and len(request.form['user_password']) > 4 and request.form['user_password'] == request.form['second_user_password']:
            hash = generate_password_hash(request.form['user_password'])
            res = dbase.addUser(request.form['user_email'], request.form['user_name'], hash)
            if res:
                return redirect('/enter')
            else:
                flash('Ошибка при добавлении в БД')
        else:
            flash('Неверно заполнены поля', 'error')
    return render_template("registration.html", menu=dbase.getMenuUser())


if __name__ == "__main__":
    app.run(port=6060)
