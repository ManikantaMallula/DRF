from rest_framework import serializers
from .models import Student, Employee

# class StudentSerialzer(serializers.Serializer):
#     name = serializers.CharField(max_length=30)
#     age = serializers.IntegerField()
#     address = serializers.CharField(max_length=30)
#     car = serializers.CharField(max_length=30)
#
#     def create(self,validated_data):
#         return Student.objects.create(**validated_data)

class EmployeeSerializer(serializers.Serializer):
    ename = serializers.CharField(max_length=20)
    eno = serializers.IntegerField()
    esal = serializers.CharField(max_length=20)
    add = serializers.CharField(max_length=20)

    def create(self,validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.ename = validated_data.get('ename', instance.ename)
        instance.eno = validated_data.get('eno', instance.eno)
        instance.esal = validated_data.get('esal', instance.esal)
        instance.save()
        return instance





