#coding=utf-8
class ParentClass:
    '''
    在Python中是通过一套命名体系来识别成约的访问范围的。
    在python中所有的以字母开头的成语名称被python命名体系自动识别为public，
    单个下划线开头的成员被识别为protected，最后双下划线开头的成员被识别为private。
    '''
    # public
    username = "developerworks"
    #protected 
    _email = "developerworks#163#.com"
    # private 
    __tel = "1391119****"
    __address = "FuJian China"
    
class SonClass(ParentClass):
      '''
      在继承中基类的构造（__init__()方法）
      不会被自动调用，它需要在其派生类的构造中亲自专门调用
      '''
      def __init__(self,name):
            self.name=name
            print "son is inited"
      def sum(self,a,b):
            print a+b
if(__name__ == "__main__"):
    s=SonClass("son")
    s.sum(10,2)
    print SonClass.username
    print SonClass._email
    print SonClass.__address
'''
son is inited
12
developerworks
developerworks#163#.com

Traceback (most recent call last):
  File "E:\pyt\trunk\2入门实践\oop\public_protected_private.py", line 26, in <module>
    print SonClass.__address
AttributeError: class SonClass has no attribute '__address'
'''
