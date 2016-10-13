#coding:utf-8
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:

    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from learn import views as learn_views  # new
from learn import test as learn_test  # new

urlpatterns = [
    #旧地址重定向到新地址
    url(r'^old/(\d+)/(\d+)/$', learn_views.old_new_redirect),
    url(r'^new/(\d+)/(\d+)/$', learn_views.new, name='new'),

    url(r'^insert/', learn_views.insert, name='insert'),
    url(r'^all/$', learn_views.all, name='all'),
    url(r'^update/$', learn_views.update, name='update'),
    url(r'^delete/$', learn_views.delete, name='delete'),
    #/add/111/222/
    url(r'^add/(\d+)/(\d+)/$', learn_views.add2, name='add2'),
    #/add/?a=4&b=5
    url(r'^add/', learn_views.add, name='add'),# new
    #启用其他模型来处理
    url(r'^test/', learn_test.demo, name='test'),# new
    url(r'^$', learn_views.home,name="home"),  # new
    url(r'^statictest/', learn_views.statictest,name="statictest"),  # static
    url(r'^upload/', learn_views.upload, name="upload"),
    url(r'^postcomment/', learn_views.postcomment, name="postcomment"),
    url(r'^login/', learn_views.login, name="login"),
    url(r'^logout/', learn_views.logout, name="logout"),
    url(r'^cookies/show_cookie/$',learn_views.show_cookie,name="show_cookie"),
    url(r'^cookies/set_cookie/$',learn_views.set_cookie,name="set_cookie"),
    url(r'^cookies/delete_cookie/$',learn_views.delete_cookie,name="delete_cookie"),
    url(r'^admin/', admin.site.urls),
]
