from typing import Any
from flaskr import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

def isEmpty(*args: str) -> bool:
    """ Check if any argument in *args is an empty string. """
    for arg in args:
        if len(arg) == 0 or arg.isspace():
            return True
    return False


def isNone(*args: Any) -> bool:
    """ Check if any argument in *args is None. """
    for arg in args:
        if arg == None:
            return True
    return False

def data_process(sql: str) -> list:
    """ Execute SQL and make data type be list. """
    datas = []
    
    tuples = db.engine.execute(sql)
    for t in tuples:
        data = {}
        #print(t._mapping.items())
        for i,j in t._mapping.items():
            print(i,j)
            data.setdefault(i,j)
        datas.append(data)
    return datas

def data_process_with_param(sql: str, param : tuple) -> list:
    """ Execute SQL and make datatype be a list. """
    datas = []
    print('sql語法:', sql)
    print('sql參數:', param)
    tuples = db.engine.execute(sql, param)
    for t in tuples:
        data = {}
        #print(t._mapping.items())
        for i,j in t._mapping.items():
            print(i,j)
            data.setdefault(i,j)
        datas.append(data)
    return datas

# 針對只要一個 attribute 的狀況
def data_process_with_special_case(sql: str) -> list:
    tuples = db.engine.execute(sql)
    return ([i[0] for i in tuples.fetchall()])

def datetime_now_to_integer():
    time=int(datetime.now().timestamp())
    std_timestamp = int(datetime(2023,4,22).timestamp())
    return(time - std_timestamp)

def datetime_to_integer(time : datetime) -> int:
    time=int(time.timestamp())
    std_timestamp = int(datetime(2023,4,22).timestamp())
    return(time - std_timestamp)

def integer_to_datetime(integer : int) -> datetime:
    std_timestamp = int(datetime(2023, 4, 22).timestamp())
    timestamp = std_timestamp + integer
    dt = datetime.fromtimestamp(timestamp)
    return dt

def check_email_exist(email: str) -> bool:
    sql: str = 'SELECT email FROM User Where email = ' + '\"' + email + '\"'
    return(data_process(sql) != [])
    
def check_email(email: str) -> bool:
    sql: str = 'SELECT * FROM User Where email = ' + '\"' + email + '\"'
    return(data_process(sql))

def check_password(answer: str, password: str) -> bool:
    ans: bool = check_password_hash(answer, password)
    return(ans)