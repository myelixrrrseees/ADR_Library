from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mnjndjks ndvdsmvdsv mkdnjcbvc nm jdnjdvnkdk 2884732 mvnjcvxvbfv1'
app.debug = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AUTH.db'
db = SQLAlchemy(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/base')
def base():
    return render_template("base_page_of_book.html")


@app.route('/enter')
def enter():
    return render_template("enter.html")


@app.route('/registr', methods=['GET', 'POST'])
def registr():
    from models import Login
    if request.method == "POST":
        name = request.form['name']
        password = request.form['password']
    
        login = Login(name=name, password=password)
    
        try:
            db.session.add(login)
            db.session.commit()
            return redirect('/')
        except:
            return "Регистрация не прошла успешно"
    else:
        return render_template("registr.html")


if __name__ == "__main__":
    app.run(debug=True)


