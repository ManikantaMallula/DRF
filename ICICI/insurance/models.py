from django.db import models


class Destination(models.Model):
    destination = models.CharField(max_length=200)

    def __str__(self):
        return str(self.destination)


class BusDetails(models.Model):
    source = models.CharField(max_length=200)
    destination_one = models.ForeignKey(Destination, on_delete=models.CASCADE)
    bus_name = models.CharField(max_length=200)
    vehicle_num = models.CharField(max_length=200)
    driver_no = models.CharField(max_length=200)
    start_time = models.TimeField()
    arrival_time=models.TimeField()
    price = models.FloatField()

    def __str__(self):
        return str(self.bus_name)


class Route(models.Model):
    origin = models.CharField(max_length=200)
    destination_two = models.ForeignKey(Destination, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.destination_two)


s = (('male',"male"),('Female','Female'),('other','other'))
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=200, choices=s)
    aadhar_no = models.IntegerField(null=True, default=True)
    bus_name = models.ForeignKey(BusDetails, on_delete=models.CASCADE,null=True,default=True)

    def __str__(self):
        return str(self.bus_name)
