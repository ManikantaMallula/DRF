from django.shortcuts import render

# Create your views here.
from datetime import *

def func1(request):
    todaydate=datetime.now()
    c={"d":todaydate}
    return render(request,'test1.html',c)
