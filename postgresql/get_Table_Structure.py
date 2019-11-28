from connect import PostGreSQL
dataBaseName = 'db_xtypt_bazxt'
userName = 'zfwman'
password = '6789@jkl'
host = '172.25.17.55'
port = '5432'


schema = "db_yw"
tablename = "t_sjrz"

# def choose_table(schema, tablename):
#     new_sql = "Select table_name,column_name,data_type,character_maximum_length from information_schema.columns where table_schema='{0}' and table_name='{1}';".format(schema, tablename)
#     return new_sql


def table_info(table_name):
    sql = f'''select a.attnum,a.attname,concat_ws('',t.typname,SUBSTRING(format_type(a.atttypid,a.atttypmod) from '\(.*\)')) as type,d.description from pg_class c,pg_attribute a,pg_type t,pg_description d
where c.relname='{table_name}' and a.attnum>0 and a.attrelid=c.oid and a.atttypid=t.oid and d.objoid=a.attrelid and d.objsubid=a.attnum;'''
    return sql

# xx = PostGreSQL(dataBaseName, userName, password, host, port)
# res = xx.ExecQuery(table_info(tablename))
# print(res)
# for item in res:
#     print('v_' + tablename + '_' + item[1] + '\t\t' + item[2] + ';' + '\t' + '--' + item[3])

