from django.contrib import admin
from .models import hostel

@admin.register(hostel)
class hostelAdmin(admin.ModelAdmin):
 list_display = ('id','hname','cno','address')
