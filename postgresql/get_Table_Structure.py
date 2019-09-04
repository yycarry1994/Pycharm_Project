from connect import PostGreSQL
dataBaseName = 'db_xtypt_bazxt'
userName = 'sa'
password = '6789@jkl'
host = '172.25.17.55'
port = '5432'


schema = "db_sacw"
tablename = "t_tj_zl"

def choose_table(schema, tablename):
    new_sql = "Select table_name,column_name,data_type,character_maximum_length from information_schema.columns where table_schema='{0}' and table_name='{1}';".format(schema, tablename)
    return new_sql

xx = PostGreSQL(dataBaseName, userName, password, host, port)
res = xx.ExecQuery(choose_table(schema, tablename))

print(res)