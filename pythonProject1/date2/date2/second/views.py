from django.shortcuts import render
import datetime
# Create your views here.
def fun2(request):
    c=datetime.datetime.now()
    a={'x':c}
    return render(request,'test2.html',a)
