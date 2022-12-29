from django.contrib import admin
from .models import Route,BusDetails, Destination, Customer

# Register your models here.

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ['id', 'origin', 'destination_two', 'date']

@admin.register(BusDetails)
class BusDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'source', 'destination_one', 'bus_name', 'vehicle_num', 'driver_no','arrival_time','start_time','price']

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['id', 'destination']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'sex', 'aadhar_no', 'bus_name']