#coding=utf-8
import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='root',
        db ='netbug',
        charset='utf8'
        )
cur = conn.cursor()

#更新
sql = "INSERT INTO layer1(`title`,`url`,`add_time`,`status`)VALUES('JAVA 软件工程师','http://xmrc.com.cn/net/info/showco.aspx?ID=1606675','1469540795','-1')"
try:
   # 执行SQL语句
   cur.execute(sql)
   # 提交到数据库执行
   conn.commit()
except:
   conn.rollback()
# 关闭数据库连接
conn.close()