from django.shortcuts import render,HttpResponse
from datetime import datetime,timedelta

# Create your views here.


def setsession(request):
    request.session['name']='ojas'
    request.session['sname'] = "innovative"
    return render(request,'sets.html')


def getsession(request):
    name = request.session.get('name')
    keys = request.session.keys()
    items = request.session.items()
    return render(request,'gets.html',{'name':name,'keys':keys,"items":items})


def delsession(request):
    request.session.flush()
    return HttpResponse('<h1> session got deleted </h1>')