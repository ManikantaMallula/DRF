from rest_framework import serializers
from .models import Employee, Educational, Personal

class Employee_serializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    
    

class Educational_serializer(serializers.ModelSerializer):
    class Meta:
        model = Educational
        fields = '__all__'
    

class Personal_serializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'
   