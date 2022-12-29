from django.contrib import admin
from .models import Employee1

# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ['id', 'ename', 'eno', 'esal']


@admin.register(Employee1)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'ename', 'eno', 'esal', 'add']