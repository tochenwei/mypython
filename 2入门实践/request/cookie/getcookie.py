#coding:utf-8
'''
cookielib模块的主要作用是提供可存储cookie的对象，以便于与urllib2模块配合使用来
访问Internet资源。Cookielib模块非常强大，我们可以利用本模块的CookieJar类的对象
来捕获cookie并在后续连接请求时重新发送，比如可以实现模拟登录功能。该模块主要的
对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。

它们的关系：CookieJar —-派生—->FileCookieJar  —-派生—–>MozillaCookieJar和LWPCookieJar
'''
import urllib2
import cookielib
#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value
'''
我们使用以上方法将cookie保存到变量中，然后打印出了cookie中的值，运行结果如下
Name = BAIDUID
Value = 2D30EB41956CE8C250BFDF82A0E94BDD:FG=1
Name = BIDUPSID
Value = 2D30EB41956CE8C250BFDF82A0E94BDD
Name = H_PS_PSSID
Value = 18881_18285_1443_18201_19671_18283_19689_19558_17001_15779_12286
Name = PSTM
Value = 1460450902
Name = BDSVRTM
Value = 0
Name = BD_HOME
Value = 0
'''