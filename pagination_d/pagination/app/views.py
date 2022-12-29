from django.shortcuts import render
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer
from .page import MyPaginaton, MYpagination2, MyPagination3


class PaginationView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer





    # pagination_class = MYpagination2
    search_fields = ('eno', )
    ordering_fields = ('eno', 'esal')


