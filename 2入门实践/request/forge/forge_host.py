#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
#通过伪造header中的host信息访问网站受限的内容
  
import urllib2
import sys
  
#抓取网页内容-发送报头-1
a = '4FA6C445329AA10050B4CC677C7473B6987DD47E5D8AEA97'
b = str(a)
url = 'http://xmrc.com.cn/net/common/getJPEG.ashx?s='+b+'&flag=1'
send_headers = {
 'Host':'xmrc.com.cn',
 'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
 'Connection':'keep-alive'
}
  
req = urllib2.Request(url,headers=send_headers)
r = urllib2.urlopen(req)
  
html = r.read()        #返回网页内容
receive_header = r.info()     #返回的报头信息
  
# sys.getfilesystemencoding() 
html = html.decode('utf-8','replace').encode(sys.getfilesystemencoding()) #转码:避免输出出现乱码 
  
print receive_header
# print '####################################'
print html
