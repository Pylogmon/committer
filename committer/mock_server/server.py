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


@server.route('/get_product', methods=['get'])
def get_product():
    path = split(realpath(__file__))[0]

    conn = sqlite3.connect(join(path, 'test.db'))
    cursor = conn.cursor()
    # 执行查询语句:
    cursor.execute('select * from Product')
    # 获得查询结果集:
    values = cursor.fetchall()
    product_list = {"status": "Success", "data": []}
    if len(values) == 0:
        product_list["status"] = "Fail"
    else:
        for i in values:
            product_list["data"].append({
                "product_id": i[0],
                "product_name": i[1]
            })
    cursor.close()
    conn.close()
    res = json.dumps(product_list)
    return res


@server.route('/get_project', methods=['get'])
def get_project():
    product_id = flask.request.args.get("product_id")
    path = split(realpath(__file__))[0]

    conn = sqlite3.connect(join(path, 'test.db'))
    cursor = conn.cursor()
    # 执行查询语句:
    cursor.execute('select * from project where product_id=?', (product_id, ))
    # 获得查询结果集:
    values = cursor.fetchall()
    project_list = {"status": "Success", "data": []}
    if len(values) == 0:
        project_list["status"] = "Fail"
    else:
        for i in values:
            project_list["data"].append({
                "project_id": i[0],
                "project_name": i[2]
            })
    cursor.close()
    conn.close()
    res = json.dumps(project_list)
    return res


@server.route('/get_module', methods=['get'])
def get_module():
    product_id = flask.request.args.get("product_id")
    project_id = flask.request.args.get("project_id")

    path = split(realpath(__file__))[0]

    conn = sqlite3.connect(join(path, 'test.db'))
    cursor = conn.cursor()
    # 执行查询语句:
    cursor.execute('select * from Module where product_id=? and project_id=?',
                   (product_id, project_id))
    # 获得查询结果集:
    values = cursor.fetchall()
    module_list = {"status": "Success", "data": []}
    if len(values) == 0:
        module_list["status"] = "Fail"
    else:
        for i in values:
            module_list["data"].append({
                "module_id": i[0],
                "module_name": i[3]
            })
    cursor.close()
    conn.close()
    res = json.dumps(module_list)
    return res


@server.route('/get_branch', methods=['get'])
def get_branch():
    product_id = flask.request.args.get("product_id")
    project_id = flask.request.args.get("project_id")
    module_id = flask.request.args.get("module_id")

    path = split(realpath(__file__))[0]

    conn = sqlite3.connect(join(path, 'test.db'))
    cursor = conn.cursor()
    # 执行查询语句:
    cursor.execute(
        'select * from Branch where product_id=? and project_id=? and module_id=?',
        (product_id, project_id, module_id))
    # 获得查询结果集:
    values = cursor.fetchall()
    branch_list = {"status": "Success", "data": []}
    if len(values) == 0:
        branch_list["status"] = "Fail"
    else:
        for i in values:
            branch_list["data"].append({
                "branch_id": i[0],
                "branch_name": i[4]
            })
    cursor.close()
    conn.close()
    res = json.dumps(branch_list)
    return res


@server.route('/commit', methods=['post'])
def commit():
    path = split(realpath(__file__))[0]
    conn = sqlite3.connect(join(path, 'test.db'))
    cursor = conn.cursor()
    body = flask.request.values.to_dict()
    cursor.execute('select password from User where user_name=?',
                   (body["user_name"], ))
    # 获得查询结果集:
    values = cursor.fetchall()

    if values[0][0] == body["password"]:
        body.pop("user_name")
        body.pop("password")
        keys = str(tuple(body.keys())).replace("'", "")
        values = str(tuple(body.values()))
        sql = f"insert into `Commit` {keys} values {values}"
        cursor.execute(sql)
        conn.commit()
        cursor.execute(
            "select * from `Commit` order by commit_id desc limit 1")
        values = cursor.fetchall()
        data = {"status": "Success", "data": {}, "message": "commit success"}
        data_list = [
            'commit_id', 'title', 'product_id', 'project_id', 'module_id',
            'branch_id', 'keywords', 'type', 'severity', 'pri', 'assigned',
            'os', 'browser', 'content', 'creator'
        ]
        for i in range(len(values[0])):
            data["data"][data_list[i]] = values[0][i]
    else:
        data = {"status": "Fail", "data": {}, "message": "Auth Fail"}
    cursor.close()
    conn.close()
    res = json.dumps(data)
    return res


# 启动服务，debug=True表示修改代码后自动重启；
# 启动服务后接口才能访问，端口号为9000，默认ip地址为127.0.0.1
server.run(port=9000, debug=True)
