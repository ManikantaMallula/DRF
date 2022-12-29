from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from .forms import stu

def show(request):
    if request.method=="POST":
        a=stu(request.POST)
        if a.is_valid():
            print('form validated')
            print('name',a.cleaned_data['name'])
            print('password',a.cleaned_data['password'])
            print('rpassword',a.cleaned_data['rpassword'])
    else:
        a=stu()
    return render(request,'test.html',{'m':a})
