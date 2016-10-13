#coding:utf-8
'''
类变量紧接在类名后面定义，相当于java和c++的static变量

实例变量在__init__里定义，相当于java和c++的普通变量
'''
class test:
    #类变量
    count = 0;
    def __init__(self, c):
        #实例变量
        self.counter = c;
        self.__class__.count = self.__class__.count + 1;
    def getCount(self):
        return self.__class__.count
		
a = test(3)
print a.counter
print test.count

b = test(-1)
print b.counter
print test.count
print b.getCount()
'''
>>> 
=============== RESTART: E:\pyt\trunk\2入门实践\oop\static.py ===============
3
1
-1
2
2
>>> 
'''
