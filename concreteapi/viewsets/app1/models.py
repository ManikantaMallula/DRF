from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    city = models.CharField(max_length=200)
