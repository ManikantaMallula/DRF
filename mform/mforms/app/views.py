from django.shortcuts import render
from app.forms import Student
from .models import stu

# Create your views here.

def show(request):
    if request.method=="POST":
        a=stu.objects.get(pk=1)
        ob=Student(request.POST,instance=a)
        if ob.is_valid():
            ob.save()
    else:
        ob=Student()
    return render(request,'test.html',{'ob':ob})