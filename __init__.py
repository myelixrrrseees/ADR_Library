from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mnjndjks ndvdsmvdsv mkdnjcbvc nm jdnjdvnkdk 2884732 mvnjcvxvbfv1'
app.debug = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AUTH.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'enter'
login_manager.init_app(app)


