#coding=utf-8
#array是一个2纬列表
array = [ ['b', 4], ['e', 2], ['a', 5], ['d', 1], ['c', 3] ]
array.sort()
print array

#按照内部列表的第2列的值进行排序
array.sort(key=lambda x:x[1])#lambda x:x[1]返回list的第二个数据
print array


'''
[['a', 5], ['b', 4], ['c', 3], ['d', 1], ['e', 2]]
[['d', 1], ['e', 2], ['c', 3], ['b', 4], ['a', 5]]
'''
