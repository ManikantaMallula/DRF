from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('home/', views.home),
    path('sign', views.sign, name='signup'),
    path('login/', views.logins, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('additem/', views.additem, name="additem"),
    path("details/<id>", views.details, name="details"),
    path('deleteb/<int:id>/', views.deleteb),
    path('deletea/<int:id>',views.deletea),

]