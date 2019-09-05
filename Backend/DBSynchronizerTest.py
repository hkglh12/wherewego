import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='aegis1load',
    db='wherewego',
    charset='utf8')

curs = conn.cursor()

sql = """insert into conntestdb(testtext)
         values(%s)"""

curs.execute(sql, ('test1'))
curs.execute(sql, ('test2'))
conn.commit()

sql = "select * from conntestdb"
curs.execute(sql)

rows = curs.fetchall()
print(rows)

conn.close()