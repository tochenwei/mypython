#coding=utf-8
import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='',
        db ='test',
        charset='utf8'
        )
cur = conn.cursor()



#查询所有
sql = "SELECT * FROM student \
       WHERE id = '%d'" % (2)
try:
   # 执行SQL语句
   cur.execute(sql)
   # 获取所有记录列表
   result = cur.fetchone()
   print result
   # 打印结果
   
except:
   print "Error: unable to fecth data"

conn.commit()
conn.close()
