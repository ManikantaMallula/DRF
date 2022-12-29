from django.db import models

# Create your models here.

class Student(models.Model):
    ename=models.CharField(max_length=30)
    eid=models.IntegerField()
    address=models.CharField(max_length=30)

    def __str__(self):
        return self.ename


