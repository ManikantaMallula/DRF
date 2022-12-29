from django.contrib import admin
from .models import Employee, Educational, Personal

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'ename', 'eid', 'role', 'salary', 'location', 'domain', 'doj']

@admin.register(Educational)
class EducationalAdmin(admin.ModelAdmin):
    list_display = ['id', 'ename', 'ssc_percentage', 'inter_percentage', 'degree_percentage', 'ssc_passoutyear', 'inter_passoutyear', 'degree_passoutyear']

@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ['id', 'ename', 'native_place', 'father_name', 'mother_name', 'dob', 'address', 'aadhar']
