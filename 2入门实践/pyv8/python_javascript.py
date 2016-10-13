#coding:utf-8
'''
http://www.jb51.net/article/44116.htm
主要介绍了pyv8学习python和javascript变量进行交互,python取得javascript里面的值、
javascript取得python里面的值、python和javascript里面的函数交互
'''
import PyV8
'''
python取得javascript里面的值
'''
with PyV8.JSContext() as env1:
    env1.eval("""
                var_i = 1;
                var_f = 1.5;
                var_s = "test";
                var_b = true;
            """)
    vars = env1.locals
    var_b = vars.var_b
    print var_b
'''
javascript取得python里面的值
'''

import PyV8
 
with PyV8.JSContext() as env1:
    env1.securityToken = "foo"
    env1.locals.prop = 3
    print int(env1.eval("prop"))

'''
python调用javascript里面的函数 
'''
import PyV8
 
with PyV8.JSContext() as ctxt:
    func = ctxt.eval("""
                    function a()
                    {
                        return "abc";
                    }
 
                    function c()
                    {
                        return "3210";
                    }
                """)
    a = ctxt.locals.a
    print a()
