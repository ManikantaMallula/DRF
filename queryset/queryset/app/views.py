from django.shortcuts import render
from .models import Employee
from django.db.models import Q
# Create your views here.

# def home(request):
#  data = Employee.objects.filter(Q(age=15))
#
# # data = Employee.objects.filter(~Q(id=6))
#
#  print("Return:", data)
#  print()
#  print("SQL Query:",data.query)
#  return render(request, 'home.html', {'data':data })


def home(request):
 data = Employee.objects.all()[5:10]
 print("Return:",data)
 print()
 print("SQL Query:",data.query)
 return render(request, 'home.html', {'data':data})


