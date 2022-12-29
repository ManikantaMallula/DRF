from django.contrib import admin
from .models import Manager


@admin.register(Manager)
class AdminHR(admin.ModelAdmin):
    list_display = ['name', 'id', 'joindate', 'sal', 'loc', 'commi']