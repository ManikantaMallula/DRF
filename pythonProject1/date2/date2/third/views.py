from django.shortcuts import render
import datetime
# Create your views here.
def fun3(request):
    c=datetime.datetime.today()
    a = {'x': c}
    return render(request,'test3.html',a)
