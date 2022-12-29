from django.shortcuts import render

from django.http import HttpResponse

from .forms import StudentReg,Employee
# Create your views here.



def show(request):
    ob=StudentReg(label_suffix="?")
    ob1=Employee(initial={'ename':'ojas'})
   # ob_order_fields(field_order=[age,name,email])
    return render(request,'test.html',{'ob':ob,"ob1":ob1})

def display(request):
    return HttpResponse("<h1>Thanks </h1>")

