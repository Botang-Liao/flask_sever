from typing import Any
from flaskr import db

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
        for i,j in t._mapping.items():
            print(i,j)
            data.setdefault(i,j)
        datas.append(data)
    return datas

