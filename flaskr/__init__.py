import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

BASE_DIR: str = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
APP_DIR: str = os.path.join(BASE_DIR, 'app')
DATABASE_DIR: str = os.path.join(BASE_DIR, 'database')
DATABASE_PATH: str = os.path.join(DATABASE_DIR, 'data.db')
USER_PICTURE_DIR: str = os.path.join(DATABASE_DIR, 'user_picture')

app = Flask(__name__, static_url_path='', static_folder=APP_DIR)

for directory in [APP_DIR, DATABASE_DIR, USER_PICTURE_DIR]:
    if not os.path.isdir(directory):
        os.mkdir(directory)

app.config['SECRET_KEY'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DATABASE_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_SORT_KEYS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from . import api_auth
from . import api_user
from . import utils
from . import user
