#encoding:utf-8

import urllib
import urllib2
#不带参数的get请求
url = "http://m.cnblogs.com/"
req = urllib2.Request(url)
print req
res_data = urllib2.urlopen(url)
res = res_data.read()
print res

#带参数的get请求
params = urllib.urlencode({'id': 8, 'name': 'jack', 'age': 25})
f = urllib2.urlopen("http://test.diyou.cc/requesttest.php?%s" % params)
print f.read()
'''
返回结果
Array
(
    [age] => 25
    [id] => 8
    [name] => jack
)
'''
