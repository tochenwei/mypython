#encoding:utf-8
import json
 
obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
encodedjson = json.dumps(obj)
'''
repr()是将一个对象转成字符串显示，注意只是显示用
'''
print repr(obj)
print encodedjson
'''
json.dumps()方法返回了一个str对象encodedjson，
我们接下来在对encodedjson进行decode，得到原始数据，需要使用的json.loads()函数：
'''
decodejson = json.loads(encodedjson)
print type(decodejson)
print decodejson[4]['key1']
print decodejson

'''
Python和JSON的数据对照表
Python           JSON
dict             object
list,tuple       array
str,unicode      string
int,long,float   number
True(注意大小写) true
False(注意大小写)false
None(注意大小写) null
'''

'''
运行结果
[[1, 2, 3], 123, 123.123, 'abc', {'key2': (4, 5, 6), 'key1': (1, 2, 3)}]
[[1, 2, 3], 123, 123.123, "abc", {"key2": [4, 5, 6], "key1": [1, 2, 3]}]
<type 'list'>
[1, 2, 3]
[[1, 2, 3], 123, 123.123, u'abc', {u'key2': [4, 5, 6], u'key1': [1, 2, 3]}]
'''

'''
json.dumps方法提供了很多好用的参数可供选择，比较常用的有sort_keys
（对dict对象进行排序，我们知道默认dict是无序存放的），separators，indent等参数。

排序功能使得存储的数据更加有利于观察，也使得对json输出的对象进行比较，例如：
'''
data1 = {'b':789,'c':456,'a':123}
data2 = {'a':123,'b':789,'c':456}
d1 = json.dumps(data1,sort_keys=True)
d2 = json.dumps(data2)
d3 = json.dumps(data2,sort_keys=True)
print d1
print d2
print d3
print d1==d2
print d1==d3

'''
输出：

{"a": 123, "b": 789, "c": 456} 
{"a": 123, "c": 456, "b": 789} 
{"a": 123, "b": 789, "c": 456} 
False 
True
'''