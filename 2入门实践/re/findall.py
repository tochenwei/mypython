#!python
#coding=utf-8
import re

p = re.compile('\d+')
m = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')

print m
'''
findall会把结果返回一个列表
现在测试这个列表是否是空的(是否有匹配到结果)
'''
if(not len(m)):
    print '0'
else:
    print len(m)
