from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.




def excp(request):
    print('printing from excp view')
    a = 10/0

    return HttpResponse('this is exception page')

def name(request):
    print('printing from name view ')
    context = {'name':"ojas"}
    return TemplateResponse(request,'name.html',context)

