from connect import PostGreSQL
from postgre_fun_title import *
from get_Table_Structure import table_info
dataBaseName = 'db_xtypt_bazxt'
userName = 'zfwman'
password = '6789@jkl'
host = '172.25.17.55'
port = '5432'
tablename = 't_sjrz'
sql_run = PostGreSQL(dataBaseName, userName, password, host, port)


print(postgre_fun_title_1)
print('\t' + postgre_fun_title_2)
print('declare')
new_sql = table_info(tablename)
res = sql_run.ExecQuery(new_sql)
all_col = []
zdname = []
all_liename = []
for item in res:
    print('\t\t' + 'v_' + tablename + '_' + item[1] + '\t\t' + item[2] + ';' + '\t' + '--' + item[3])
    col = ('\t\t' + 'v_' + tablename + '_' + item[1] + '\t:=')
    all_col.append(col)
    lie_name = ('v_' + tablename + '_' + item[1])
    all_liename.append(lie_name)
    zdname.append(item[1])
print('\t\t' + 'BEGIN')
print('\t\t' + 'for i in 1 .. cycleCount loop')
for i in range(len(all_col)):
    print('\t\t' + str(all_col[i]) + ';')
str_zdname = ",".join(zdname)
str_all_liename = ",".join(all_liename)
print('\t\t\t\t' + f"INSERT INTO db_yw.{tablename}({str_zdname})")
print('\t\t\t\t' + f'VALUES({str_all_liename})' + ';')
print('\n\n\t\t' + 'end loop;')
print('\t\t' + "RETURN 'success';")
print('end')
print('$BODY$')
print('\t' + 'LANGUAGE plpgsql VOLATILE')
print('\t' + 'COST 100')