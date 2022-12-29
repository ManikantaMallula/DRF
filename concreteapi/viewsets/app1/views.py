from django.shortcuts import render
from .models import Employee
from .serializers import StudentSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework import generics

class Studentlist(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = StudentSerializer

class Studentdetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = StudentSerializer


