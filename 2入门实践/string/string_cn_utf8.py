#coding=utf-8

#求utf-8中文字符串的长度
def str_len(str):
    try:
        row_l=len(str)
        utf8_l=len(str.encode('utf-8'))
        return (utf8_l-row_l)/2+row_l
    except:
        return None
    return None
text=u"中国1"
print str_len(text)
print len(text)
'''
4
2
'''
"""判断一个unicode是否是汉字"""
def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False
sl = list(text)
print sl
for item in sl:
    print is_chinese(item)
'''
5
3
[u'\u4e2d', u'\u56fd', u'1']
True
True
False
'''
