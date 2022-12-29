from django.shortcuts import render

def home(request):
   return render(request,"add.html")

def cal(request):
   num1=int(request.GET['num1'])
   num2=int(request.GET['num2'])
   result=num1+num2
   return render(request,"result.html",{'result':result})