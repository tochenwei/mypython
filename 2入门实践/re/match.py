#!python
#coding=utf-8
import re

p = re.compile('ab*')
m = p.match('absolutely')

if m:

    print 'Match found: ', m.group()
    #start()返回匹配开始的位置,end()返回匹配结束的位置
    print m.start(),m.end()
    #span()返回一个元组包含匹配 (开始,结束) 的位置
    print m.span()

else:

    print 'No match'
print p
'''
Match found:  ab
0 2
(0, 2)
<_sre.SRE_Pattern object at 0x0000000002ABEAB0>
'''