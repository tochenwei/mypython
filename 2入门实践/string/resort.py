#!python
#coding:utf-8
'''
对一个字符串进行重新排序
'''
s = "string"
l = list(s)
#顺序排列
l.sort()
s = "".join(l)
print s

print "\n"
#倒序排列
l=reversed(l)
s = "".join(l)
print s

'''
ginrst


tsrnig
'''
