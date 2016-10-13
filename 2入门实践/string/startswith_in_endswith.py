#encoding:utf-8
'''
测试字符串的开头和结尾、是否包含某字符串
'''
#是否是以某字符串结尾
name=raw_input("whats your name?")
if name.endswith("william"):
    print 'hello william'
#大的字符串中是否包含某小的字符串
elif 'middle' in name:
    print 'hello middle'
#是否是以某字符串开头
elif name.startswith("china"):
    print 'hello china'
else:
    print 'hello master'
