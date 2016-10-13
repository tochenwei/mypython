#!python
#coding:utf-8
'''
贪婪匹配
'''
import re
s = '<html><head><title>Title</title>'

print len(s)


print re.match('<.*>', s).span()

print re.match('<.*>', s).group()
'''
解决方案是使用不贪婪的限定符 *?、+?、?? 或 {m,n}?，尽可能匹配小的文本
'''
print re.match('<.*?>', s).group()
'''
32
(0, 32)
<html><head><title>Title</title>
<html>
'''
