from django.http import HttpResponse
from django.shortcuts import render
import datetime


def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    names="my first test,真酷"
    now=datetime.datetime.now()
    return render(request, 'runoob.html', {"name":now})

def hello(request):
    return HttpResponse("hello world!")

def login(request):

    return render(request,'index.html',)
