from django.db import models

class Employee(models.Model):
    ename = models.CharField(max_length=20)
    eno = models.IntegerField()
    esal = models.CharField(max_length=20)
