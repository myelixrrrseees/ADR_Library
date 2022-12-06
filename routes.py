from flask import Flask, render_template, request, redirect, url_for, flash

from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import app, db


@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/mainpage')
def main_page():
    return render_template("mainpage.html")


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
def regestration():
    from models import Users

    if request.method == "POST":

        email = request.form['user_email']
        name = request.form['user_name']
        password = request.form['user_password']
        second_password = request.form['second_user_password']

        user = Users.query.filter_by(email=email)

        if user :
            flash('Email already exists')
            return redirect('/regestration')

        if second_password == password:

            login = Users(email=email, name=name, password=generate_password_hash(password))

            db.session.add(login)
            db.session.commit()
            return redirect('/mainpage')
        else:
            flash('Password is not correct. Try one more.')
            return redirect('/regestration')

    else: return render_template("regestration.html")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
