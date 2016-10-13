#coding:utf-8
'''
纯http post提交
'''
import urllib2, urllib
data = {'name' : 'www', 'password' : '123456'}
f = urllib2.urlopen(
        url     = 'http://test.diyou.cc/requesttest.php',
        data    = urllib.urlencode(data)
  )
print f.read()
'''
返回值
Array
(
    [password] => 123456
    [name] => www
)
'''
