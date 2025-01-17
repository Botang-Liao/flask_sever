from flask import request, jsonify, abort
from flask.wrappers import Response
from flaskr import app
from flaskr.utils import *
from flask_login import current_user, login_required
from model.user import User
from typing import Any, Dict, List, Union
from werkzeug.security import generate_password_hash, check_password_hash

app_route = '/api/user/'

# 新增活動
@app.route(app_route + "add-post", methods=['POST'])
@login_required
def add_post():
    data: dict = request.get_json()
    keys =', '.join(['uid', 'time'] + list(data.keys())) 
    params = [current_user.id, datetime_now_to_integer()] + list(data.values())
    qm = '?, ' * (len(params)-1) + '?'
    params = tuple(params) 
    
    try:
        sql = 'INSERT INTO Post (' + keys + ') VALUES (' + qm + ')'
        #sql = 'INSERT INTO Post (uid,  time, activity, title, about, date, address,number_of_people_limitation, space_available, content, latitude, longitude, expected_cost_lowerbound, expected_cost_upperbound) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'
        db.engine.execute(sql, params)
    except:
        abort(400)
    return jsonify(success=True), 200


# 參加活動
@app.route(app_route + "join-post", methods=['POST'])
@login_required
def join_post():
    data: dict = request.get_json()
    keys =', '.join(list(data.keys())) 
    params = list(data.values())
    qm = '?, ' * (len(params)-1) + '?'
    params = tuple(params) 
    
    #sql = "SELECT * FROM User WHERE uid = " + str(current_user.id)
    #datas = data_process(sql)

    try:
        sql = 'INSERT INTO Participant (' + keys + ') VALUES (' + qm + ')'
        db.engine.execute(sql, params)
        sql = 'UPDATE Post SET space_available=space_available-? WHERE pid=?'
        db.engine.execute(sql, (data['number'], data['pid']))
    except:
        abort(400)
    
    return jsonify(success=True), 200

@app.route('/')
def hello():
    return "Hello world"

# 得到使用者的資訊
@app.route(app_route + "get-info", methods=['GET'])
@login_required
def user_get_info():
    #(str(current_user.id))
    sql = "SELECT * FROM User WHERE uid = ?"
    datas = data_process(sql, str(current_user.id))
    datas[0].pop('password_hash', None)
    return jsonify(datas[0])

# 得到活動資訊
@app.route(app_route + "get-post-info", methods=['GET'])
#@login_required
def get_post_info():
    param = str(request.args.get('type','0'))  
    sql = "SELECT title, about, date, address, number_of_people_limitation, space_available, "
    sql += "content, expected_cost_lowerbound, expected_cost_upperbound FROM Post, Activity WHERE acid = activity"
    if param == '0':
        datas = data_process(sql)
    else:
        sql += (" AND atid = ?") 
        datas = data_process(sql, param)
    
    return jsonify(datas)

# 得到揪團類型資訊
@app.route(app_route + "get-activity-type-info", methods=['GET'])
#@login_required
def get_activity_type_info():
    sql = "SELECT name FROM ActivityType"
    datas = data_process_with_special_case(sql)
    return jsonify(datas)

# 得到活動資訊
@app.route(app_route + "get-activity-info", methods=['GET'])
#@login_required
def get_activity_info():
    param = str(request.args.get('type','0'))  
    sql = 'SELECT name FROM Activity'
    if param == '0':
        datas = data_process_with_special_case(sql)
    else:
        sql += (' WHERE atid = ?') 
        datas = data_process_with_special_case(sql, param)
    return jsonify(datas)

# 修改使用者資訊
@app.route(app_route + "set-info", methods=['POST'])
#@login_required
def set_info():
    data: dict = request.get_json()

    if isEmpty(data['email'], data['username'], data['password']):
        abort(400)

    sql = "SELECT * FROM User WHERE uid = ?;"
    datas = data_process_with_param(sql, (current_user.id))[0]
    tuples = []
    for i in datas:
        if (i == 'password') and (not isEmpty(data[i])):
            tuples.append(generate_password_hash(data[i]))
        else:
            tuples.append(data[i])

    tuples.append(datetime_now_to_integer()) 
    tuples.append(current_user.id)
    sql = "UPDATE User SET email=?, username=?, password_hash=?, education=?, about=?, language=?, other_info=?, last_edit=? WHERE uid = ?"
    tuples = tuple(tuples)
    #print(tuples)
    db.engine.execute(sql, tuples)
    #print(datas)

    return jsonify(success=True), 200
    
