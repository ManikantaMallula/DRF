from django.db import models

# Create your models here.
class Manager(models.Model):

    name=models.CharField(max_length=30)
    id=models.IntegerField(primary_key=True)
    joindate=models.DateField()
    sal=models.FloatField()
    loc=models.CharField(max_length=30)
    commi=models.FloatField()