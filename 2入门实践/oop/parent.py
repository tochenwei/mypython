#coding=utf-8
class ParentClass:
        def __init__(self,name):
            self.name=name
            print "parent is inited"
if(__name__ == "__main__"):
        b=ParentClass('father')
