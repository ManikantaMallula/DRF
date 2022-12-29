from django.contrib import admin

# Register your models here.


from app1.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=('id','ename','eid')

admin.site.register(Student,StudentAdmin)

