#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
#通过伪造header中的referer信息访问网站受限的内容
  
import urllib2
import sys
  
a = '4FA6C445329AA10050B4CC677C7473B6987DD47E5D8AEA97'
b = str(a)
url = 'http://xmrc.com.cn/net/common/getJPEG.ashx?s='+b+'&flag=1'

req = urllib2.Request(url)
req.add_header('Referer','http://xmrc.com.cn/net/info/showco.aspx?CompanyID=558109')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
r = urllib2.urlopen(req)
  
html = r.read()
receive_header = r.info()
  
html = html.decode('utf-8').encode(sys.getfilesystemencoding())
  
print receive_header
print '#####################################'
print html