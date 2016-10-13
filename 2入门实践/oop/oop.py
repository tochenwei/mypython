#coding=utf-8
class Base:
    def __init__(self):
        self.data = []
        #往数组中顺序插入元素
    def add(self, x):
        self.data.append(x)
        #根据数值删除元素
    def delete(self, x):
        self.data.remove(x)
        #根据索引删除元素
    def delete_by_index(self,i):
        del self.data[i]
# Child extends Base
class Child(Base):
    def plus(self,a,b):
        return a+b
oChild =Child()
oChild.add("str1")
print oChild.data
print "\r\n"
#打印list所有元素
print oChild.data[0:]

'''
下面是模拟一个数组按照数值删除指定元素的例子
'''
oChild.delete("str1")
print oChild.data
'''
下面是模拟一个数组按照索引删除指定元素的例子
(删除第2个元素)
'''
oChild.add("abc")
oChild.add("str1")
oChild.add("str2")
oChild.delete_by_index(1)
print oChild.data
print "\r\n"
#打印除了最后一个元素以外的所有元素
print oChild.data[0:-1]

'''
下面是一个加法运算的例子
'''
print oChild.plus(2,3)
