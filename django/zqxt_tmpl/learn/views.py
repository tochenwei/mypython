#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
 
def home(request):
    List = map(str, range(100))# 一个长度为100的 List
    return render(request, 'home.html', {'List': List})
def login(request):
    List = map(str, range(100))
    return render(request, 'login.html', {'List': List})
	
def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
