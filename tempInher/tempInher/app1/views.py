from django.shortcuts import render

# Create your views here.
def func3(request):
    return render(request,"reg.html")

def func4(request):
    return render(request,"base.html")