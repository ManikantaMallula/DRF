from django.contrib import admin
from .models import Customer, Category, Product, Cart, Cartitem


# @register.admin(Customer)
# class CustomerAdmin()


admin.site.register([Customer, Category, Product, Cart, Cartitem])