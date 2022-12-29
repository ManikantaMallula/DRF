from django.contrib import admin
from app1.models  import Emp
# Register your models here.

@admin.register(Emp)
class ModelAdminEmp(admin.ModelAdmin):
    list_display=('ename','eid','salary','address','email','image','description','Indian','c','phone')

