from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def func3(request):
    return HttpResponse("<h1>This is cources app and 1st function</h1>")

def func4(request):
    return HttpResponse("<h1>This is cources app and 2nd function</h1>")