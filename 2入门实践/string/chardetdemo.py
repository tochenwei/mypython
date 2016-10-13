#coding:utf-8
'''
到http://pypi.python.org/pypi/chardet#downloads下载chardet-2.3.0.tar.gz；
解压到site-package文件夹.
Python及其一些模块安装包里可能有setup.py，是用来执行安装的。
C:\Python27\Lib\site-packages\chardet-2.3.0
比如要安装chardet-2.3.0，进入到chardet-2.3.0的解压包里，执行：python setup.py install
就可以完成安装了。
'''
import urllib
rawdata = urllib.urlopen('http://www.baidu.com/').read()
import chardet
print chardet.detect(rawdata)
'''
返回值会是类似这样的 
一个是检测的可信度，另外一个就是检测到的编码。
{'confidence': 0.99, 'encoding': 'utf-8'}
'''
