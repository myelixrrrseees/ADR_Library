from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import app, db


@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/mainpage')
def main_page():
    return render_template("main_page.html")


@app.route('/library')
def library():
    return render_template("library.html")


@app.route('/enter')
def enter():
    return render_template("enter.html")


@app.route('/news')
def news():
    return render_template("news.html")



@app.route('/regestration', methods=['GET', 'POST'])
def registr():
    from models import Login

    if request.method == "POST":

        name = request.form['user_name']
        password = request.form['user_password']
        second_password = request.form['second_user_password']

        if second_password == password:
    
            login = Login(name=name, password=password)
        
            try:
                db.session.add(login)
                db.session.commit()
                return redirect('/')
            except:
                return "Нет"
        else:
            return redirect('/regestration')
    else:
        return render_template("regestration.html")


if __name__ == "__main__":
    app.run(debug=True)
