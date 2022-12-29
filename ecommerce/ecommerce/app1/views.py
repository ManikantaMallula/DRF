from django.shortcuts import render

# Create your views here.

def func1(request):
    return render(request,"home.html")

def func2(request):
    return render(request,"login.html")

def func3(request):
    return render(request,"grocery.html")

def func4(request):
    return render(request,"mobiles.html")


def func5(request):
    return render(request,"fashion.html")

