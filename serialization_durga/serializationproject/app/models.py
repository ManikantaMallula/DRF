from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=30)
    car = models.CharField(max_length=30)


class Employee(models.Model):
    ename = models.CharField(max_length=20)
    eno = models.IntegerField()
    esal = models.CharField(max_length=20)

