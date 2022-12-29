from django.db import models

# Create your models here.
class Dashboard(models.Model):
    Title = models.CharField(max_length=15)
    Description = models.TextField()

class ContactModel(models.Model):
    Name = models.CharField(max_length=30)
    email= models.EmailField()
    MobileNo = models.IntegerField()
    City = models.CharField(max_length=10)








