#coding:utf-8
from function import *

from MySQL import *
import time

dbconfig = {'host':'127.0.0.1', 
            'port': 3306, 
            'user':'root', 
            'passwd':'root', 
            'db':'netbug', 
            'charset':'utf8'}
      
#连接数据库，创建这个类的实例
db = MySQL(dbconfig)

start_time = time.time()
#bsql = 'SET UNIQUE_CHECKS=0'
#db.query(bsql)

for i in range(20000001,25000001):
    stri = str(i)
    vmd5 = md5(stri)
    vsha1 = sha1(stri)
    sql="INSERT INTO raintable2(`str`,`vmd5`,`vsha1`)VALUES('"+stri+"','"+vmd5+"','"+vsha1+"')"
    #print sql
    try:
        db.query(sql)
        db.commit()
    except:
        db.rollback()
    #关闭数据库
db.close()

end_time = time.time()
#esql = 'SET UNIQUE_CHECKS=1'
#db.query(esql)
print 'time taken(s):'
print end_time-start_time
