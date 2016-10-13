#coding=utf-8
#字符串截取
word="abcdefg"
print word

print word[2]   #截取下标为2的字符串，得到c

print word[1:3]  #截取下标从1到3的字符串，得到bc

print word[:2]   #截取前2个字符串,得到ab

print word[-1]   #截取最后一个字符串,得到g

print word[-2:]  #截取最后2个字符串

print word[:-2]  #截取除了最后2个字符串以外的内容 "abcde"

#字符串替换(替换空格和末尾的逗号)
s = 'abcd,,,,,,';
s = s.strip().lstrip().rstrip(',')
print s

#连接字符串
sStr1 = 'hello '
sStr2 = 'world'
sStr1 += sStr2
print sStr1

#比较字符串
sStr1 = 'strchr'
sStr2 = 'strch'
print cmp(sStr1,sStr2)

#扫描字符串是否包含指定的字符
#find()方法：查找子字符串，若找到返回从0开始的下标值，若找不到返回-1
info = 'abca'
print info.find('a')##从下标0开始，查找在字符串里第一个出现的子串，返回结果：0

info = 'abca'
print info.find('a',1)##从下标1开始，查找在字符串里第一个出现的子串：返回结果3

info = 'abca'
print info.find('333')##返回-1,查找不到返回-1


#字符串长度
sStr1 = 'strlen'
print len(sStr1)

#将字符串中的大小写转换
sStr1 = 'JCstrlwr'
sStr1 = sStr1.upper()
#sStr1 = sStr1.lower()
print sStr1

#追加指定长度的字符串
sStr1 = '12345'
sStr2 = 'abcdef'
n = 3
sStr1 += sStr2[0:n]
print sStr1

#复制指定长度的字符
sStr1 = ''
sStr2 = '12345'
n = 3
sStr1 = sStr2[0:n]
print sStr1

#将字符串前n个字符替换为指定的字符
sStr1 = '12345'
ch = 'r'
n = 3
sStr1 = n * ch + sStr1[3:]
print sStr1

#翻转字符串
sStr1 = 'abcdefg'
sStr1 = sStr1[::-1]
print sStr1
#查找字符串
sStr1 = 'abcdefgh'
sStr2 = 'cde'
print sStr1.find(sStr2)

print sStr1

#PHP 中 addslashes 的实现
def addslashes(s):
    d = {'"':'\\"', "'":"\\'", "\0":"\\\0", "\\":"\\\\"}
    return ''.join(d.get(c, c) for c in s)
 
s = "John 'Johny' Doe (a.k.a. \"Super Joe\")\\\0"
print s
print addslashes(s)

"""
abcd
hello world
1
4
6
JCSTRLWR
12345abc
123
rrr45
gfedcba
2
abcdefgh

"""
