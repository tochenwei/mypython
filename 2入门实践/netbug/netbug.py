#coding=utf-8
'''
实现一个简单的网络爬虫功能
    将一个url地址下的图片通过正则表达式的匹配下载到本地
'''
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

    
def getImg(html):
    '''
	re模块主要包含了正则表达式：

　　re.compile() 可以把正则表达式编译成一个正则表达式对象.

　　re.findall() 方法读取html 中包含 imgre（正则表达式）的数据。

    这里的核心是用到了urllib.urlretrieve()方法，直接将远程数据下载到本地。

　　通过一个for循环对获取的图片连接进行遍历，为了使图片的文件名看上去更规范，
    对其进行重命名，命名规则通过x变量加1。保存的位置默认为程序的存放目录。

	程序运行完成，将在目录下看到下载到本地的文件。
	'''
    reg = r'src="(.+?\.jpg)" size='
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0

    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1 
    return imglist
html = getHtml("http://tieba.baidu.com/p/4434948359")
print getImg(html)