from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=40)
    marked_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='img')




class Cart_items(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)





