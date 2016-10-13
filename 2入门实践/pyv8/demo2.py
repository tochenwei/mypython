
import PyV8
class Test:
 
    def jstest(self):        
        ctxt = PyV8.JSContext()
        ctxt.enter()               
        func = ctxt.eval('''(function(){return '###'})''')
        print func()
        func = ctxt.eval('''(function(a,b){return a+b})''')
        print func(1,3)
        print '213'

if __name__ == '__main__':
 
    crawler = Test()    

    crawler.jstest()
