from django.db import models

# Create your models here.

class stu(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    password=models.CharField(max_length=30)