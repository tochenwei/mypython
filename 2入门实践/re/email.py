#!python
#coding:utf-8
'''
邮箱的正则表达式匹配
'''
import re
s='fds 1105258@qq.com 55533@163.com'
'''
\b	匹配一个单词边界，也就是指单词和空格间的位置。例如，“er\b”可以匹配“never”中的“er”，但不能匹配“verb”中的“er”。
\B	匹配非单词边界。“er\B”能匹配“verb”中的“er”，但不能匹配“never”中的“er”。
'''
regex = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b", re.IGNORECASE)
mails = re.findall(regex, s)
print mails

'''
['1105258@qq.com', '55533@163.com']
'''
