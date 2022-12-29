from django.db import models

# Create your models here.

class hostel(models.Model):
    hname=models.CharField(max_length=15)
    cno=models.IntegerField()
    address=models.TextField()
