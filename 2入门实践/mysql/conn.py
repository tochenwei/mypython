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

#创建数据表
'''
cur.execute("CREATE TABLE IF NOT EXISTS `student` (\
  `id` int(11) NOT NULL AUTO_INCREMENT,\
  `name` varchar(20) CHARACTER SET utf8 DEFAULT NULL,\
  `class` varchar(30) DEFAULT NULL,\
  `age` varchar(10) DEFAULT NULL,\
  PRIMARY KEY (`id`)\
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;")
'''

#插入一条数据
cur.execute("insert into student(`name`,`class`,`age`) values('Tom','3 year 2 class','9')")
cur.execute("insert into student(`name`,`class`,`age`) values('汉朝','3 year 2 class','90')")
iname='iname'
iclass='iclass34'
iage='56'
cur.execute("insert into student(`name`,`class`,`age`) values('%s','%s','%s')" %(iname,iclass,iage))

#修改查询条件的数据
cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
cur.execute("delete from student where age='9'")


#查询所有
sql = "SELECT * FROM student \
       WHERE id < '%d'" % (100002)
try:
   # 执行SQL语句
   cur.execute(sql)
   # 获取所有记录列表
   results = cur.fetchall()
   # 打印结果
   print results
except:
   print "Error: unable to fecth data"


conn.commit()
conn.close()
