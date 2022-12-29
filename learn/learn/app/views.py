from django.shortcuts import render

# Create your views here.
def func1(request):
    return render(request,"test1.html")

def func2(request):
    return render(request,"test2.html")

def func3(request):
    return render(request,"test3.html")

def func4(request):
    return render(request,"nav.html")