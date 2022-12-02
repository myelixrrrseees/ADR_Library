from config import db


class Login(db.Model):
    __tablename__ = 'auth'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer())
    pages = db.Column(db.Integer())