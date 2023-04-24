from typing import Any
from flaskr import db
from datetime import datetime

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

# 針對只要一個 attribute 的狀況
def data_process_with_special_case(sql: str) -> list:
    tuples = db.engine.execute(sql)
    return ([i[0] for i in tuples.fetchall()])

def datetime_to_integer(time=int(datetime.now().timestamp())):
    std_timestamp = int(datetime(2023,4,22).timestamp())
    return(time - std_timestamp)

