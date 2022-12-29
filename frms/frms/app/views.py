from django.shortcuts import render
from app.forms import Stu
from django.http import HttpResponseRedirect

def fun(request):
    return render(request,'reg.html')

def show(request):
    if request.method=='POST':
        s=Stu(request.POST)
        if s.is_valid():
            print("form validated")
            name=s.cleaned_data['name']
            age=s.cleaned_data['age']
            print('name',name)
            print('age',age)
            return HttpResponseRedirect('/show/1/')
    else:
        s=Stu()
    return render(request,'reg.html',{'s':s})
# Create your views here.
'''
def fun(request):
    s=Stu(auto_id=True,label_suffix="$",initial={'name':"ojas"})
    s.order_fields(field_order=['age','name','email','key'])
    return render(request,'reg.html',{'s':s})  '''


