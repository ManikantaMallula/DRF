from django.shortcuts import render

# Create your views here.

def func1(request):
    return render(request,"home.html")
def func2(request):
    return render(request,"contact.html")
def func3(request):
    return render(request,"nav.html")
