from django.shortcuts import render

# Create your views here.

def func4(request):
    return render(request,'home.html')

def func2(request):
    return render(request,'cont.html')

def func3(request):
    return render(request,'skills.html')
def func1(request):
    return render(request,'base.html')