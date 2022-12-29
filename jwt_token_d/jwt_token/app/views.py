from django.shortcuts import render
from .models import Employee1
from .serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet

# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.simplejwt.autherntication import JWTAutherntication
from rest_framework.permissions import IsAuthenticated




class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee1.objects.all()
    serializer_class = EmployeeSerializer

    authentication_classes = [JWTAutherntication,]
    permission_classes = [IsAuthenticated,]



