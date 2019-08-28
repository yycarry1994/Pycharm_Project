import psycopg2
import json

def get_data(sql):
    con = psycopg2.connect(database='db_xtypt_bazxt', user='sa', password='6789@jkl', host='172.25.17.55', port='5432')
    run_sql = con.cursor()
    run_sql.execute(sql)
    res = run_sql.fetchall()
    for row in res:
        yield {
            'c_bh' : row[0],
            'c_pttyah' : row[1],
            'c_ajmc' : row[2],
            'c_gaajbh' : row[3],
            'c_gaajwh' : row[4],
            'c_tysah' : row[5]
        }
    return res
    con.close()


sql = 'select c_bh,c_pttyah,c_ajmc,c_gaajbh,c_gaajwh,c_tysah from db_sacw.t_aj_jbxx limit 10'
aa = []
for item in get_data(sql):
    aa.append(item)
aa1 = json.dumps(aa, sort_keys=True, indent=4)

print(aa1)





