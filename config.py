from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mnjndjks ndvdsmvdsv mkdnjcbvc nm jdnjdvnkdk 2884732 mvnjcvxvbfv1'
app.debug = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AUTH.db'
db = SQLAlchemy(app)