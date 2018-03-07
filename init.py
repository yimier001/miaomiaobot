import pymysql

db = pymysql.connect("172.21.0.10","root","testpwd1","test",port=5000 )

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS playerinfo")
cursor.execute("DROP TABLE IF EXISTS schedule")

sch = ["Wed"]
name = ["111"]
time = ["19:00"]

type = ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]

sql = """CREATE TABLE schedule (
         sch CHAR(30),
         name CHAR(30),
         time CHAR(30),
         num INT )"""
cursor.execute(sql)

sql = """CREATE TABLE playerinfo (
         sch CHAR(32),
         id INT,
         type CHAR(32),
         uid CHAR(32),
         name CHAR(32) )"""
cursor.execute(sql)

for i in range(len(sch)):
    sql = """INSERT INTO schedule VALUES ('%s', '%s', '%s', 0)"""%(sch[i],name[i],time[i])
    cursor.execute(sql)
    for j in range(1,26):
        sql = """INSERT INTO playerinfo VALUES ('%s', %d, '%s', '', '')"""%(sch[i],j,type[j])
        cursor.execute(sql)

db.close()