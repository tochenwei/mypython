#coding:utf-8
class CC(object):
    #我是Python类默许的，没重写__init__,所以也没有什么特殊操作
    pass


class C(object):
    def __init__(self,name,phone,ID):
        super(C,self).__init__()
        self.name = name
        self.phone = phone
        self.id = ID
        print u"Hi man 我重写了__init__,因为我需要更多的操作"

cc = CC() # 创建CC实例
c = C('BeginMan','110','12306') # 创建C实例