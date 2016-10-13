#coding:utf-8
'''
交换两个变量的值
也许你见到过这样的情况，但是你知道它是如何工作的吗？ 
首先，逗号是元组构造语法。
等号的右边是定义一个元组 (tuple packing).
其左边为一个目标元组 (tuple unpacking)).
右边的元组根据名称被 unpacked 到左边的无组。
>>> a=1
>>> b=2
>>> b,a=a,b
>>> a
2
>>> b
1
>>> 
'''
'''
交换两个变量的值
'''
a=1
b=2
b,a=a,b
print a
print b
