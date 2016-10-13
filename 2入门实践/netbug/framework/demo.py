#coding:utf-8
#Filename:demo.py
from core.url import *
from core.MySQL import *

import re
from lxml import etree
import datetime
import time

import ConfigParser
import string, os, sys
cf = ConfigParser.ConfigParser() 
cf.read("netbug.conf")
def runNetBug(currentUrl):
    global cf
    #read by type
    db_host = cf.get("db", "db_host")
    db_port = cf.getint("db", "db_port")
    db_user = cf.get("db", "db_user")
    db_pass = cf.get("db", "db_pass")
    db_name = cf.get("db", "db_name")

    #currentUrl= "http://xmrc.com.cn/net/info/resultg.aspx?a=a&g=g&jobtype=&releaseTime=365&searchtype=1&keyword=java&sortby=updatetime&ascdesc=Desc"
    result = getUrlContent(currentUrl)
    #print result
     
    page = etree.HTML(result)

    list1 = page.xpath(u"//table[@class=\"text-center queryRecruitTable\"]/tr[@class=\"bg\"]")
    #print list1
    count = len(list1) #求出外层的行数
    #print count
    if count>0:
        #数据库连接参数  
        dbconfig = {'host':db_host, 
            'port': db_port, 
            'user':db_user, 
            'passwd':db_pass, 
            'db':db_name, 
            'charset':'utf8'}
      
        #连接数据库，创建这个类的实例
        db = MySQL(dbconfig)
        for i in range(1,count+1):
            title = page.xpath(u"//table[@class=\"text-center queryRecruitTable\"]/tr[@class=\"bg\"]"+"["+str(i)+"]/td[2]//text()")
            title_str = ''.join(title)
            title_str = title_str.replace("\r",'').replace("\n",'').replace("\t",'')
            title_str = title_str.strip()
            #print title_str
            company = page.xpath(u"//table[@class=\"text-center queryRecruitTable\"]/tr[@class=\"bg\"]"+"["+str(i)+"]/td[3]//text()")
            company_str = ''.join(company)
            company_str = company_str.replace("\r",'').replace("\n",'').replace("\t",'')
            company_str = company_str.strip()
            
            
            ltext2 = page.xpath(u"//table[@class=\"text-center queryRecruitTable\"]/tr[@class=\"bg\"]"+"["+str(i)+"]/td[2]//a[1]/@href")
            for a in ltext2:
                url = makeFullUrl(currentUrl,a)
            t = str(time.mktime(datetime.datetime.now().timetuple())) #t = 1469541223.0
            time_str = t[:-2]  #time_str = 1469541223
            sql="INSERT INTO layer1(`title`,`company`,`url`,`add_time`,`status`)VALUES('"+title_str+"','"+company_str+"','"+url+"','"+time_str+"','-1')"
            #print sql
            try:
                db.query(sql)
                db.commit()
            except:
                db.rollback()
            #关闭数据库
        db.close()
    

    epage            = cf.getint("layer1", "epage")
    startPageNum     = cf.getint("layer1", "startPageNum")
    pageParam        = cf.get("layer1", "pageParam")
    pageSetp         = cf.get("layer1", "pageSetp")
    #自动翻页，收集下一页数据
    if count==epage:
        nextPageNum      = getNextPageNum(currentUrl,pageParam,startPageNum,pageSetp)
        nextPage=getNextPageUrl(currentUrl,pageParam,nextPageNum)
        runNetBug(nextPage)

if __name__ == '__main__':
    currentUrl= "http://xmrc.com.cn/net/info/resultg.aspx?a=a&g=g&jobtype=&releaseTime=365&searchtype=1&keyword=java&sortby=updatetime&ascdesc=Desc"
    runNetBug(currentUrl)
