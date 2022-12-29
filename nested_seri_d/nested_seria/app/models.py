from django.db import models

class Employee(models.Model):
    ename = models.CharField(max_length=20)
    eno = models.IntegerField()
    esal = models.CharField(max_length=20)

    def __str__(self):
        return self.ename

class Personal(models.Model):
    ename = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='empmodel')
    father_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)
