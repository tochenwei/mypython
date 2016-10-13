#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    List = map(str, range(100))# 一个长度为100的 List
    return render(request, 'home.html', {'string': string,'TutorialList': TutorialList,'info_dict': info_dict,'List':List})
def statictest(request):
    return render(request, 'static.html')        
def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))
def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
    
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
def new(request, a, b):
    c = int(a) + int(b)
    return HttpResponse('new address:'+str(c))
def old_new_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('new', args=(a, b))
    )

from learn.models import Person
# 数据库操作
def insert(request):
	#test1= Person(name='李磊')
	if len(request.GET['realname'])==0:
		return HttpResponse("<p>请输入真实姓名！</p>")
	if len(request.GET['realname'])>20:
		return HttpResponse("<p>不能超过20个字符！</p>")
	test1= Person(name=request.GET['realname'])
    #把年龄设置为一个随机数
	import random
	test1.age  =  random.randint(1, 20)
	test1.save()
	return HttpResponse("<p>数据添加成功！</p>")
# 数据库操作
def all(request):
	# 初始化
	response = ""
	response1 = ""
	
	
	# 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
	list = Person.objects.all()
		
	# filter相当于SQL中的WHERE，可设置条件过滤结果
	response2 = Person.objects.filter(id=1) 
	
	# 获取单个对象
	response3 = Person.objects.get(id=1) 
	
	# 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
	Person.objects.order_by('name')[0:2]
	
	#数据排序
	Person.objects.order_by("id")
	
	# 上面的方法可以连锁使用
	Person.objects.filter(name="w3cschool.cc").order_by("id")
	
	# 输出所有数据
	for var in list:
		response1 += var.name + " "
	response = response1
	return HttpResponse("<p>" + response + "</p>")
    
#修改
def update(request):
	# 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
	test1 = Person.objects.get(id=1)
	test1.name = 'w3cschool菜鸟教程'
	test1.save()
	
	# 另外一种方式
	#Test.objects.filter(id=1).update(name='w3cschool菜鸟教程')
	
	# 修改所有的列
	# Test.objects.all().update(name='w3cschool菜鸟教程')
	
	return HttpResponse("<p>修改成功</p>")
#删除   
def delete(request):
    # 删除id=1的数据
    test1 = Person.objects.get(id=100)
    test1.delete()
	# 另外一种方式
	# Test.objects.filter(id=1).delete()
	# 删除所有数据
	# Test.objects.all().delete()
    return HttpResponse("<p>删除成功</p>")
def upload(request):
    if request.method == 'POST':
        file_url=handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        '''
        返回值:upload/2016/07/20/83025aafa40f4bfbc55b19e3014f78f0f63618f9.gif
        '''
        return HttpResponse(file_url)
    else:
        return render(request, 'upload.html', {'what': 'file upload'})
    
 
def handle_uploaded_file(file, filename):
    import os
    import time
    upload_dir='upload/'
    if not os.path.exists(upload_dir):
        os.mkdir(upload_dir)
    #path = upload_dir + time.strftime('%Y/%m/%d/%H/%M/%S/')
    path = upload_dir + time.strftime('%Y/%m/%d/')
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = path + filename
    with open(file_name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
    return file_name
'''
@description:session的应用,2个例子
'''
def postcomment(request):
    #第一次访问的时候
    if request.session.get('has_commented', False):
        return HttpResponse("You've already commented.")

    request.session['has_commented'] = True
    return HttpResponse('Thanks for your comment!')
def login(request):
    #m = Member.objects.get(username=request.POST['username'])
    #if m.password == request.POST['password']:
        request.session['member_id'] = 10
        return HttpResponse("You're logged in.member_id="+str(request.session.get('member_id')))
    #else:
    #    return HttpResponse("Your username and password didn't match.")
              
def logout(request):
    HttpResponse(request.session.get('member_id'))
    #删除session
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.member_id="+str(request.session.get('member_id')))
###############################################################
#一、存取Cookies

#   1、设置Cookies
#       response.set_cookie("cookie_key","value")
#   2、获取Cookies
#       value = request.COOKIES["cookie_key"]
#   3、删除Cookies
#       response.delete_cookie("cookie_key",path="/",domain=name)
#   4、检测Cookies
#       if "cookie_name" is request.COOKIES :
#   5、response.set_cookie() 传递一些可选的参数 描述
#       参数      缺省值       描述
#       max_age  None  cookies的持续有效时间（以秒计），如果设置为 None cookies 在浏览器关闭的时候就失效了。
#       expires  None  cookies的过期时间，格式： "Wdy, DD-Mth-YY HH:MM:SS GMT" 如果设置这个参数，
#                           它将覆盖 max_age 参数。
#       path      "/"     cookie生效的路径前缀，浏览器只会把cookie回传给带有该路径的页面，这样你可以避免将
#                           cookie传给站点中的其他的应用。
#                           当你的应用不处于站点顶层的时候，这个参数会非常有用。
#       domain      None    cookie生效的站点。你可用这个参数来构造一个跨站cookie。如， domain=".example.com"
#                           所构造的cookie对下面这些站点都是可读的： www.example.com 、 www2.example.com 和
#                           an.other.sub.domain.example.com 。
#                           如果该参数设置为 None ，cookie只能由设置它的站点读取。
#       secure      False  如果设置为 True ，浏览器将通过HTTPS来回传cookie。
#二、Cookies规则
#    1、Cookies是以字典方式存储，（Key—>Value的键值对方式存储），访问是只要访问Session的键就可以得到键对应的Value
#       如果：value = response.set_cookie("cookie_key","value")
#    2、存储到客户端
#       优点：
#           数据存在在客户端，减轻服务器端的压力，提高网站的性能。
#       缺点：
#           1、安全性不高：在客户端机很容易被查看或破解用户回话信息
##################################################################
import datetime
def set_cookie(request,hour=0,name="admin"):
    dt = datetime.datetime.now() + datetime.timedelta(hours = int(hour))
    html ="设置用户%s为登录回话,过期时间：%s" % (name,str(dt))
    response = HttpResponse(html)
    response.set_cookie("username",name,expires=dt)
    return response

def show_cookie(request):
    html = ""
    if "username" in request.COOKIES :
        name = request.COOKIES["username"]
        if name == "admin":
            html = "用户%s 的Cookies 没有超时" % name
        if name == "loker" :
            html = "用户%s 的Cookies 没有超时" % name
        else: 
            #过期时间为1小时以后
            dt = datetime.datetime.now() + datetime.timedelta(hours = int(1))
            name ="loker"
            html ="用户的Cookies 已经超时\n设置用户%s为登录回话,过期时间：%s" % (name,str(dt))
            response = HttpResponse(html)
            response.set_cookie("username",name,expires=dt)
            return response
    response = HttpResponse(html)
def delete_cookie(request):
    html = ""
    response = HttpResponse(html)
    if "username" in request.COOKIES :
        name = request.COOKIES["username"]

    if "username" in request.COOKIES :   
    #   删除Cookies   
        response.delete_cookie("username",path="/")
    return HttpResponse(name)