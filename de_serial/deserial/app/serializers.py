from rest_framework import serializers
from .models import Student

class Studentserial(serializers.Serializer):
    name = models.CharField(max_length=40)
    rno = models.IntegerField()
    city = models.CharField(max_length=40)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
