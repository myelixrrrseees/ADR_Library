from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_user
from __init__ import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import app
from models import db
from models import Users


@login_manager.user_loader
def load_user(id):
    return Users.query.get(id)


@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/library')
def library():
    return render_template("library.html")


@app.route('/enter', methods=['GET', 'POST'])
def enter():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        remember = True if request.form.get('remember') else False

        user = Users.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect('/enter')
        login_user(user, remember=remember)
        return redirect('/library')
    else:
        return render_template("enter.html")


@app.route('/regestration', methods=['GET', 'POST'])
def regestration():
    if request.method == "POST":

        email = request.form['user_email']
        name = request.form['user_name']
        password = request.form['user_password']
        second_password = request.form['second_user_password']

        user = Users.query.filter_by(email=email, name=name).first()

        if user:
            flash('Email already exists')
            return redirect('/regestration')

        if second_password == password:

            login = Users(email=email, name=name, password=generate_password_hash(password))

            db.session.add(login)
            db.session.commit()
            return redirect('/library')
        else:
            flash('Second password is not correct. Try one more.')
            return redirect('/regestration')

    else:
        return render_template("regestration.html")


if __name__ == "__main__":
    app.run(debug=True, port=6060)
