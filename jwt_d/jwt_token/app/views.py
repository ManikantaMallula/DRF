from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee1
from .serializers import EmployeeSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import  IsAuthenticated



class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee1.objects.all()
    serializer_class = EmployeeSerializer

    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAuthenticated,]


