#coding:utf-8
'''
在另一个包里引用其他包的资源方法1
'''
import sys
sys.path.append("..")
print(sys.path)
from subPack1.module_11 import funcA
funcA()



'''
在另一个包里引用其他包的资源方法2
'''
import sys
import os
sys.path.append(os.getcwd()+"\\.."+'\\subPack1')
print(sys.path)
from module_11 import *
funcA()

