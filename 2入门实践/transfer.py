#coding=utf-8
'''
各种数据类型的转换
@author:chenwei
@date:2016-07-12
'''
'''
一、int函数能够
     （1）把符合数学格式的数字型字符串转换成整数
     （2）把浮点数转换成整数，但是只是简单的取整，而非四舍五入。
'''
aa = int("124")    #Correct
print "aa = ", aa  #result=124
bb = int(123.45)   #correct
print "bb = ", bb  #result=123
#cc = int("-123.45")  #Error,Can't Convert to int
#print "cc = ",cc
#dd = int("34a")      #Error,Can't Convert to int
#print "dd = ",dd
#ee = int("12.3")     #Error,Can't Convert to int
#print ee
print '------------------------\n';
'''
二、float函数将整数和字符串转换成浮点数。
'''
aa = float("124")     #Correct
print "aa = ", aa     #result = 124.0 
bb = float("123.45")  #Correct
print "bb = ", bb     #result = 123.45
cc = float('-123.6')    #Correct
print "cc = ",cc      #result = -123.6
dd = float("-123.34") #Correct
print "dd = ",dd      #result = -123.34
#ee = float('123v')    #Error,Can't Convert to float
#print ee
print '------------------------\n';
'''
三、str函数将数字转换成字符
'''
aa = str(123.4)     #Correct
print aa            #result = '123.4'
#bb = str(-124.a)    #SyntaxError: invalid syntax
#print bb
cc = str(-123.45) #correct
print cc            #result = '-123.45'
dd = str('ddd')     #correct
print dd            #result = ddd
ee = str(-124.3)    #correct
print ee            #result = -124.3
'''
float(x)
float()函数把一个数字或字符串转换成浮点数
'''
print float("12")
print '------------------------\n';

#1、字典
dict = {'name': 'Zara', 'age': 7, 'class': 'First'}

#字典转为字符串，返回：<type 'str'> {'age': 7, 'name': 'Zara', 'class': 'First'}
print type(str(dict)), str(dict)

#字典可以转为元组，返回：('age', 'name', 'class')
print tuple(dict)
#字典可以转为元组，返回：(7, 'Zara', 'First')
print tuple(dict.values())

#字典转为列表，返回：['age', 'name', 'class']
print list(dict)
#字典转为列表
print dict.values

#2、元组
tup=(1, 2, 3, 4, 5)

#元组转为字符串，返回：(1, 2, 3, 4, 5)
print tup.__str__()

#元组转为列表，返回：[1, 2, 3, 4, 5]
print list(tup)

#元组不可以转为字典

#3、列表
nums=[1, 3, 5, 7, 8, 13, 20];

#列表转为字符串，返回：[1, 3, 5, 7, 8, 13, 20]
print str(nums)

#列表转为元组，返回：(1, 3, 5, 7, 8, 13, 20)
print tuple(nums)

#列表不可以转为字典

#4、字符串

#字符串转为元组，返回：(1, 2, 3)
print tuple(eval("(1,2,3)"))
#字符串转为列表，返回：[1, 2, 3]
print list(eval("(1,2,3)"))
#字符串转为字典，返回：<type 'dict'>
print type(eval("{'name':'ljq', 'age':24}"))
