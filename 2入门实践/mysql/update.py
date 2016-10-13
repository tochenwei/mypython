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

#更新
sql = "update student SET age='89'\
       WHERE id = '%d'" % (2)
try:
   # 执行SQL语句
   cur.execute(sql)
   # 提交到数据库执行
   conn.commit()
except:
   conn.rollback()
# 关闭数据库连接
conn.close()