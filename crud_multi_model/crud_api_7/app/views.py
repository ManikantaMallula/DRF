from django.shortcuts import render
from .models import Employee, Educational, Personal
from .serializer import Employee_serializer, Educational_serializer, Personal_serializer
from rest_framework.views import APIView, Response, status
from rest_framework import status


class EmployeeApiView(APIView):

    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Employee.objects.get(id=id)
            serializer = Employee_serializer(stu)
            print(serializer)
            return Response(serializer.data)
        stu = Employee.objects.all()
        serializer = Employee_serializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        serializer = Employee_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        id = pk
        stu = Employee.objects.get(pk=id)
        serializer = Employee_serializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "complete data updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, format=None):
        id = pk
        stu = Employee.objects.get(pk=id)
        serializer = Employee_serializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "complete data updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id = pk
        stu = Employee.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'data deleted'})

class EducationalApiView(APIView):

    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Educational.objects.get(id=id)
            serializer = Educational_serializer(stu)
            print(serializer)
            return Response(serializer.data)
        stu = Educational.objects.all()
        serializer = Educational_serializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        serializer = Educational_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        id = pk
        stu = Educational.objects.get(pk=id)
        serializer = Educational_serializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "complete data updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, format=None):
        id = pk
        stu = Educational.objects.get(pk=id)
        serializer = Educational_serializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "complete data updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id = pk
        stu = Educational.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'data deleted'})


class PersonalApiView(APIView):

    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Personal.objects.get(id=id)
            serializer = Employee_serializer(stu)
            print(serializer)
            return Response(serializer.data)
        stu = Employee.objects.all()
        serializer = Employee_serializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        serializer = Personal_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        id = pk
        stu = Personal.objects.get(pk=id)
        serializer = Personal_serializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "complete data updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, format=None):
        id = pk
        stu = Personal.objects.get(pk=id)
        serializer = Personal_serializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "complete data updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id = pk
        stu = Personal.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'data deleted'})


