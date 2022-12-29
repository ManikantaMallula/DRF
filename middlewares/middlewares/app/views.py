from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    print('printing from view function')

    return HttpResponse("this is home page")