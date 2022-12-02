import flask
import json
import sqlite3
from os.path import join, split, realpath
# 创建接口后台服务，方便请求接口
server = flask.Flask(__name__)


# 装饰器，将login()函数变为一个接口 127.0.0.1:9000/login
@server.route('/login', methods=['post'])
def login():
    username = flask.request.args.get("user_name")
    password = flask.request.args.get("password")
    status = None
    message = None
    path = split(realpath(__file__))[0]

    conn = sqlite3.connect(join(path, 'test.db'))
    cursor = conn.cursor()
    # 执行查询语句:
    cursor.execute('select password from User where user_name=?', (username, ))
    # 获得查询结果集:
    values = cursor.fetchall()
    if len(values) == 0:
        status = "Fail"
        message = "User does not exist"
    else:
        if values[0][0] == password:
            status = "Success"
            message = "Login Success"
        else:
            status = "Failed"
            message = "Wrong Password"
    cursor.close()
    conn.close()
    res = json.dumps({"status": status, "message": message})
    return res


@server.route('/get_user', methods=['get'])
def get_user():
    path = split(realpath(__file__))[0]

    conn = sqlite3.connect(join(path, 'test.db'))
    cursor = conn.cursor()
    # 执行查询语句:
    cursor.execute('select * from User')
    # 获得查询结果集:
    values = cursor.fetchall()
    user_list = {"status": "Success", "data": []}
    if len(values) == 0:
        user_list["status"] = "Fail"
    else:
        for i in values:
            user_list["data"].append({"user_id": i[0], "user_name": i[1]})
    cursor.close()
    conn.close()
    res = json.dumps(user_list)
    return res


# 启动服务，debug=True表示修改代码后自动重启；
# 启动服务后接口才能访问，端口号为9000，默认ip地址为127.0.0.1
server.run(port=9000, debug=True)
