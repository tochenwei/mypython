#coding:utf-8
'''
函数中的静态成员变量的实现方式
'''
def mystaticfun():
    if not hasattr(mystaticfun, "counter"): #(1)
        #如果没有被定义过，开始初始化.
        mystaticfun.counter=0  #initialization call is inside the function
    else:
        mystaticfun.counter+=1
    print mystaticfun.counter

mystaticfun()
mystaticfun()
mystaticfun()
