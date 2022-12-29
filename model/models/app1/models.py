from django.db import models

# Create your models here.
class Emp(models.Model):
    ename=models.CharField(max_length=30,primary_key=True)
    eid=models.IntegerField(Notnull=False)
    address=models.CharField(max_length=30)
    salary=models.FloatField()
    email=models.EmailField()
    image=models.BinaryField()
    description=models.TextField(max_length=30)
    Indian=models.BooleanField()
    c=models.URLField()
    phone=models.BigIntegerField()


