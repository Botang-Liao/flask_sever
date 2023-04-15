from flask import request, jsonify, abort
from flaskr import app
from flaskr.utils import *
from flask_login import current_user, login_required
from flaskr.user import User

app_route = '/api/user/'


@app.route('/')
def hello():
    return "Hello world"

# 得到使用者的資訊
@app.route(app_route + "get-info", methods=['GET'])
@login_required
def user_get_info():
    print(str(current_user.id))
    sql = "SELECT * FROM User WHERE uid = " + str(current_user.id)
    datas = data_process(sql)
    datas[0].pop('password_hash', None)
    return jsonify(datas)

# 得到活動資訊
@app.route(app_route + "get-activity-info", methods=['GET'])
@login_required

def get_activity_info():
    param = str(request.args.get('param','0'))  
    sql = "SELECT * FROM Post, Activity WHERE atid = " + param + " AND acid = activity" if param != '0' else "SELECT * FROM Post, Activity WHERE acid = activity"
    datas = data_process(sql)
    return jsonify(datas)

