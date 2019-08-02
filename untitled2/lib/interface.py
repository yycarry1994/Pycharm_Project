'''
2019/06/18
'''
import flask
import redis
from lib.tool import conn_mysql, md5_pass, my_json
from conf.setting import MYRDS_PORT, MYRDS_HOST, RDS_DB
from flask import request
from data.msg import NOT_NULL
server_login = flask.Flask(__name__)
server_sign = flask.Flask(__name__)

@server_login.route('/login', methods=['post'])
def login():
    username = request.values.get("username")
    password = request.values.get("password")
    password = md5_pass(password)
    if username and password:
        r1 = redis.Redis(host=MYRDS_HOST, port=MYRDS_PORT, db=RDS_DB)
        keys = r1.keys()
        if username.encode() in keys:
            return {'msg': '你已登录', 'code': 800}
        else:
            sql = 'select id,username,password from user where username ="%s";' % username
            res =conn_mysql(sql)
            if not res:
                return "{'code': 200, 'msg': '用户名或密码错误'}"
            elif res['password'] == password:
                return "{'code': 200, 'msg': '登录成功'}"
            else:
                return "{'code': 200, 'msg': '用户名或密码错误'}"
    else:
        return my_json(NOT_NULL)



@server_sign.route('/sign', methods=['post'])
def sign():
    username = request.values.get("username")
    password = request.values.get("password")
    password = md5_pass(password)
    if username and password:
        sql = 'select id,username,password from user where username ="%s";' % username
        res = conn_mysql(sql)
        if res:
            return '{"code":200, "msg":"用户名重复"}'
        else:
            sql1 = 'insert into user value (123, "%s", "%s");' % (username, password)
            conn_mysql(sql1)
            return '{"code":200, "msg":"注册成功"}'
    else:
        return my_json(NOT_NULL)