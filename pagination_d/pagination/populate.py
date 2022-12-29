import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pagination.settings')
import django
django.setup()


from app.models import Employee
from faker import Faker
from random import *
faker=Faker()

def populate(n):
    for i in range(n):
        no = randint(1001, 9999)
        name = faker.name()
        sal = randint(10000, 20000)
        emp_record = Employee.objects.get_or_create(eno=no, esal=sal, ename=name)
populate(120)

