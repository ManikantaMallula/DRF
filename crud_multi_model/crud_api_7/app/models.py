from django.db import models

class Employee(models.Model):
    ename = models.CharField(max_length=50)
    eid = models.IntegerField()
    role = models.CharField(max_length=50)
    salary = models.IntegerField()
    location = models.CharField(max_length=50)
    domain = models.CharField(max_length=50)
    doj = models.CharField(max_length=50)

    def __str__(self):
        return self.ename


class Educational(models.Model):
    ename = models.ForeignKey(Employee, on_delete=models.CASCADE)
    ssc_percentage = models.IntegerField(default=True, null=True)
    inter_percentage = models.IntegerField(default=True, null=True)
    degree_percentage = models.IntegerField(default=True, null=True)
    ssc_passoutyear = models.DateField(default=True, null=True)
    inter_passoutyear = models.DateField(default=True, null=True)
    degree_passoutyear = models.DateField(default=True, null=True)




class Personal(models.Model):
    ename = models.ForeignKey(Employee, on_delete=models.CASCADE)
    native_place = models.CharField(max_length=50,default=True, null=True)
    father_name = models.CharField(max_length=50, default=True, null=True)
    mother_name = models.CharField(max_length=50, default=True, null=True)
    dob = models.DateField(default=True, null=True)
    address = models.CharField(max_length=50, default=True, null=True)
    aadhar = models.IntegerField(default=True, null=True)






