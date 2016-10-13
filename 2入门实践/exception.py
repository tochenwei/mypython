#coding=utf-8
'''
Python中的异常类型
-----
1、NameError：尝试访问一个未申明的变量

2、ZeroDivisionError：除数为0

3、SyntaxError：语法错误

4、IndexError：索引超出范围

5、KeyError：字典关键字不存在

6、IOError：输入输出错误

7、AttributeError：访问未知对象属性

8、ValueError：数值错误

9、TypeError：类型错误

10、AssertionError：断言错误
'''
s=raw_input("Input your age:")
if s =="":
    raise Exception("Input must no be empty.")
try:
    i=int(s)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unknown exception!"
else: # It is useful for code that must be executed if the try clause does not raise an exception
    print "You are %d" % i," years old"
finally: # Clean up action
    print "Goodbye!"
