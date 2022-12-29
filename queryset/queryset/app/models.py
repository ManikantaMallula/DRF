from django.db import models

# Create your models here.

class Employee(models.Model):
 name = models.CharField(max_length=70)
 age = models.IntegerField(unique=True, null=False)
 city = models.CharField(max_length=70)
 salary = models.IntegerField()
