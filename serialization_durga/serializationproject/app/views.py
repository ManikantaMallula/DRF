from django.shortcuts import render
from .models import Student, Employee
from .serializers import EmployeeSerializer
from django.views.generic import View
import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from django.http import HttpResponse

# class StudentCRUDCBV(View):
#     def get(self, request, id, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pdata = JSONParser().parse(stream)
#         id = pdata.get(id,None)
#
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerialzer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type = 'application/json')
#
#         qs = Student.objects.all()
#         serializer = StudentSerialzer(qs, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type = 'application/json')


class EmployeeCBSCRUD(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get(id, None)

        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json')
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json')

    def post(self, request, *args, **kwargs):

        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=pdata)

        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'user created succussfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data)

    def put(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp, data=pdata, partial=True)

        if serializer.is_valid():
            serializer.save()
            msg = {'msg':'resource updated succussfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type = 'application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser.parse(stream)
        id = pdata.get('id')
        emp = Employee.objects.get(id=id)
        emp.delete()