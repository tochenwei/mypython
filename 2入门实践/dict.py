'''
字典的组成：字典是由大括号{  }来包含其数据的，大括号内包含键和其对应的值，
一对键和值成为一个项。键和值用冒号:隔开，项和项之间用逗号,号隔开。
空字典就是不包含任何项的大括号，像{ }这样就是一个空字典。
'''
#一个字典
dict1 = {'name':'chenwei','age':'31'}
print(dict1)
print(dict1['name'])
#添加字典项目
dict1['gender']='man'
print(dict1)
#修改字典项目
dict1['name']='william'
print(dict1)
#删除字典项目
del(dict1['age'])
print(dict1)
'''
clear方法：清空字典内容，变量名.clear()
'''
dict1.clear()
print(dict1)
'''
移除字典数据pop()方法的作用是：删除指定给定键所对应的值，返回这个值并从字典中把它移除。
'''
dict2 = {'name':'gelin','age':'3'}
print(dict2)
p=dict2.pop('name')
print(p)
print(dict2)

'''
将字典other中的元素加到dict中，key重复时将用other中的值覆盖
'''
dict = {"name":"nico", "age":23}  
other = {"name":"jack", "abcd":123}  
dict.update(other)
print dict

'''
{'age': '31', 'name': 'chenwei'}
chenwei
{'gender': 'man', 'age': '31', 'name': 'chenwei'}
{'gender': 'man', 'age': '31', 'name': 'william'}
{'gender': 'man', 'name': 'william'}
{}
{'age': '3', 'name': 'gelin'}
gelin
{'age': '3'}
{'abcd': 123, 'age': 23, 'name': 'jack'}
'''