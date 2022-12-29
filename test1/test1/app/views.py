from django.shortcuts import render

from django.http import HttpResponse
import json



def details(request):
    stu_data = {
        'name':'jonny',
        'age':22,
        'address':'Hyd',
    }
    resp = '<h1>name{}<br>age{}<br>address{}<h1>'.format(stu_data['name'], stu_data['age'], stu_data['address'])
    return HttpResponse(resp)

def jsondata(request):
    stu_data = {
        'name':'sunny',
        'age':22,
        'address':'mumbai',
    }
    j_data = json.dumps(stu_data)
    return HttpResponse(j_data, content_type='application/json')






