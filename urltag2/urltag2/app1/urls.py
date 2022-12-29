
from django.urls import path
from . import views

urlpatterns = [
    path("",views.func1,name='home'),
    path("1/",views.func2,name='contact'),

]