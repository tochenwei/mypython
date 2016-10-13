#coding:utf-8
'''
@description:演示如何使用工具类调试、打印变量
'''
from var_dump import *

class A:
    def __init__(self,aa,bb):
        self.a = aa
        self.b = bb

    def pa(self):
        print(self.a,self.b)

class B:
    def __init__(self):
        self.y = 13423
        self.g = 'sdsdsds'
        self.ob = A(223,454)
        a = A(3,4)

a = B()
var_dump(a)
print('---------------------')
s = var_dump_s(a)
print type(s)
print(s)
'''
#0 object(B) (3)
    y => int(13423) 
    ob => object(A) (2)
        a => int(223) 
        b => int(454) 
    g => str(7) "sdsdsds"
---------------------
<type 'str'>
B{y=>13423, ob=>A{a=>223, b=>454}, g=>"sdsdsds"}
'''