from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse
def func(request):
    return render(request,"test1.html")

def func1(request):
    return render(request,"test2.html")

def func2(request):
    return render(request,'test3.html')
def func3(request):
    return render(request,"test4.html")
def func4(requet):
    return render(request,"test5.html")