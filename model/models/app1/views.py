from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def add(request):
    val1=int((request.GET['num1']))
    val2=int((request.GET['num2']))
    res=val1+val2
    return render(request,'add.html',{"result":res})



def show(request):
    num1=request.GET["NUM1"]
    num2=request.GET["num2"]
    all=request.GET
    det=Emp.objects.all()
    result=num+num2
    return render(request,'add.html',{ 'result':result,'all':all})