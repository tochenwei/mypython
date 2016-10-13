#coding:utf-8
import urllib
import urllib2
import cookielib

filename = 'logincookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
			'username':'test',
			'pwd':'123456'
		})
#登录URL
loginUrl = 'http://test.diyou.cc/logintest.php?act=login'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)
print result.read()
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是查询信息用
gradeUrl = 'http://test.diyou.cc/logintest.php?act=info'
#请求访问成绩查询网址
result = opener.open(gradeUrl)
print result.read()
'''
以上程序的原理如下

创建一个带有cookie的opener，在访问登录的URL时，
将登录后的cookie保存下来，然后利用这个cookie来访问其他网址。
运行结果
Array
(
    [act] => login
    [username] => test
    [pwd] => 123456
)

Array
(
    [act] => info
)
test
'''