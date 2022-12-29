from django.shortcuts import render
import datetime
# Create your views here.
def fun1(request):
    c=datetime.datetime.now()
    a = {'x': c}
    return render(request,'test1.html',a)
