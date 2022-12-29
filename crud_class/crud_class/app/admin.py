from django.contrib import admin
from .models import ContactModel,Dashboard
# Register your models here.
@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','Name','email','MobileNo','City']
@admin.register(Dashboard)
class AddAdmin(admin.ModelAdmin):
    list_display = ['id','Title','Description']