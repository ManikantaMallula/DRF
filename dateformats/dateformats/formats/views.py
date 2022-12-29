from django.shortcuts import render
from datetime import *
# Create your views here.
def func(request):
    d={"a":datetime.now()}

    return render(request,"test.html",d)