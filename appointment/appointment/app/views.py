from django.shortcuts import render
from app.forms import Pat,Schol,forth,feedback
# Create your views here.
from django.http import HttpResponse


def func(request):
    a=Pat()
    return render(request,'test.html',{'a':a})

def func1(request):
    b=Schol()
    return render(request,'Schol.html',{'b':b})
def func2(request):
    c=feedback()
    return render(request,'feedb.html',{'c':c})


def func3(request):
    d=forth()
    return render(request,'forth.html',{'d':d})

def res(request):
    return HttpResponse("<h1> Succuessful </H1>")