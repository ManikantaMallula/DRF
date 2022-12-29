from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def func1(request):
    return HttpResponse("<h1>This is trainers app and 1st function</h1>")

def func2(request):
    return HttpResponse("<h1>This is trainers app and 2nd function</h1>")