from django.urls import path
from . import views

urlpatterns=[

    path("",views.func1),
    path("one",views.func2),
    path("2",views.func3),
    path("4",views.func4),
]