#coding:utf-8
'''
类中的静态方法、类方法、实例方法
'''
class Foo(object):
    name='foo'
    def test(self):#定义了实例方法
        print("object")
        print self.name
    @classmethod
    def test2(clss):#定义了类方法
        print("class")
        print clss.name
    @staticmethod
    def test3():#定义了静态方法
        print("static")
        #print self.name #这样访问是错误的
        print Foo.name   #这样访问是正确的
ff = Foo()     
ff.test()#通过实例调用
Foo.test(ff)#直接通过类的方式调用，但是需要自己传递实例引用 
print "\n"
Foo.test2()
print "\n"
ff.test3()#使用实例调用
Foo.test3()#直接静态方式调用
'''
object
foo
object
foo


class
foo


static
foo
static
foo
'''
