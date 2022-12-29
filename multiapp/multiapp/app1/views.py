from django.shortcuts import render

# Create your views here.


def func1(request):
    return render(request,"test1.html")