'''
2019/06/18
'''
from conf.setting import MYSQL_HOST, MYSQL_PORT, SQL_DB, SALT

def md5_pass(str):
    import hashlib
    str =str +SALT
    md = hashlib.md5()
    md.update(str.encode())
    res = md.hexdigest()
    return res.upper()

def conn_mysql(sql):
    import pymysql
    conn = pymysql.connect(host=MYSQL_HOST, user='root', password='123', db=SQL_DB, charset='utf8', port=MYSQL_PORT)
    cur = conn.cursor()
    cur.execute(sql)
    res = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return res

def my_json(dic):
    import json
    return json.dumps(dic, ensure_ascii=False)

