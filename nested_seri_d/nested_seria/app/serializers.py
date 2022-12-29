from .models import Employee, Personal
from rest_framework import serializers


class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    empmodel = PersonalSerializer(read_only=True, many=True)
    class Meta:
        model = Employee
        fields = '__all__'