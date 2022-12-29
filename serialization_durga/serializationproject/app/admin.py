from django.contrib import admin
from .models import Student, Employee



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ['name', 'age', 'address', 'car']


@admin.register(Employee)
class EmploeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'ename', 'eno', 'esal']