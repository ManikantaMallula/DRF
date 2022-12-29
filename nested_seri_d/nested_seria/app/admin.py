from django.contrib import admin
from .models import Employee, Personal

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'ename', 'eno', 'esal']

@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ['id', 'ename', 'father_name', 'mother_name']