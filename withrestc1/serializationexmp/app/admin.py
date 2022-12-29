from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmploeeAdmin(admin.ModelAdmin):
    fields = ['id', 'ename', 'eno', 'esal']
