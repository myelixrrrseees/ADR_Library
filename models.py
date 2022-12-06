from __init__ import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class Users(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


class Books(db.Model):
    __tablename__ = 'Books'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer())
    pages = db.Column(db.Integer())





