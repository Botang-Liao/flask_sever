import inspect
from datetime import timedelta
from typing import Union

from flask import request, jsonify, abort
from flask.wrappers import Response
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.datastructures import FileStorage
from flaskr.user import *
from flaskr import app
#from flaskr.models import User, UserVerificationCode
from flaskr.utils import *

URL_PREFIX: str = '/api/auth/'

# 確認 email
@app.route(URL_PREFIX + 'check-email', methods=['GET'])
def auth_check_email():
    email: str = request.args.get('email', '')
    
    if isEmpty(email) or check_email_exist(email=email):
        return jsonify(valid=False)

    return jsonify(valid=True)

# 登入
@app.route(URL_PREFIX + 'login', methods=['POST'])
def auth_login():
    email: str = request.values.get('email', '')
    password: str = request.values.get('password', '')
    user_info: list = check_email(email)
    if (user_info==[]) or (not check_password(user_info[0]['password_hash'],password)):
        abort(401)
    user = User(user_info[0]['uid'])
    login_user(user)
    return Response(status=200)

# 登出
@app.route(URL_PREFIX + 'logout', methods=['POST'])
#@login_required
def auth_logout():
    logout_user()
    return Response(status=200)


@app.route(URL_PREFIX + 'signup', methods=['POST'])
def auth_sign_up():
    email: str = request.values.get('email', '')
    username: str = request.values.get('username','')
    password: str = request.values.get('password', '')
    if isEmpty(email, username, password):
        abort(400)
    if check_email_exist(email=email):
        abort(403)
    sql = 'INSERT INTO User (email, username, password_hash, verified, last_edit) VALUES (' + '\"' + email  +'\", ' + '\"' + username +'\", ' + '\"' + password +'\", ' +'0' + ', ' + str(datetime_to_integer()) + ');'
    db.engine.execute(sql)
    return Response(status=200)


def check_email_exist(email: str) -> bool:
    sql: str = 'SELECT email FROM User Where email = ' + email
    return(data_process(sql) != [])
    
def check_email(email: str) -> bool:
    sql: str = 'SELECT * FROM User Where email = ' + email
    return(data_process(sql))

def check_password(answer: str, password: str) -> bool:
    #ans: bool = check_password_hash(answer, password)
   
    ans: bool = (answer == password)
    print('ans :', answer)
    print('check_password :', ans)
    return(ans)
