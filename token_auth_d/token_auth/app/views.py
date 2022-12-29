from django.shortcuts import render
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, \
    DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

from .permissions import ReadOnly, IsGetorPatch, Alex


# class EmployeeCrudCbv(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [DjangoModelPermissions, ]


# class EmployeeCrudCbv(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [ReadOnly,]

# class EmployeeCrudCbv(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsGetorPatch,]


class EmployeeCrudCbv(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [Alex,]