import flask
import json

# 创建接口后台服务，方便请求接口
server = flask.Flask(__name__)

all_user = [{
    'id': 1,
    'sex': 1,
    'real_name': '小花'
}, {
    'id': 2,
    'sex': 0,
    'real_name': '小明'
}, {
    'id': 3,
    'sex': 0,
    'real_name': '小黑'
}]


# 装饰器，将get_all_user()函数变为一个接口 127.0.0.1:9000/get_user
@server.route('/get_user', methods=['get', 'post'])
def get_all_user():
    res = json.dumps(all_user, ensure_ascii=False)
    return res


# 启动服务，debug=True表示修改代码后自动重启；
# 启动服务后接口才能访问，端口号为9000，默认ip地址为127.0.0.1
server.run(port=9000, debug=True)
