from .models import Employee1
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee1
        fields = '__all__'

