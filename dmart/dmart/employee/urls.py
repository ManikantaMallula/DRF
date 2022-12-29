from django.urls import path
from . import views

urlpatterns = [
    path('c', views.func1),
    path('d', views.func2),

]