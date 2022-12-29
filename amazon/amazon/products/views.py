from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def func(request):
    return HttpResponse("<h1>products list</h1>")