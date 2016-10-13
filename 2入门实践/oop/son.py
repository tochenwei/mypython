#coding=utf-8
import parent

class SonClass(parent.ParentClass):#继承父类,这里一定要写模块名.类名
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
