from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100, null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=40)
    slug = models.SlugField(unique=True)
    marked_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="img")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    warrentty = models.CharField(max_length=20, null=True, blank=True)
    return_policy = models.CharField(max_length=40,null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.PositiveIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'cart: '+str(self.id)

class Cartitem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    sub_total = models.PositiveIntegerField()

    def __str__(self):
        return 'Cart: '+str(self.cart.id)+'Cartitem: '+str(self.id)


