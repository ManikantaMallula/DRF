from django.urls import path
from insurance import views
from django.contrib import admin

urlpatterns=[
    path('home/',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('signup/', views.User_SignUp, name='signup'),
    path('login/', views.User_Login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('profile/', views.profile,name='profile'),
    path('about/',views.About,name='about'),
    path('buslist/',views.buslist,name='buslist'),
    path('customer/', views.customer, name='customer'),
    path('confirm/', views.confirm, name='confirm'),
    path('success/', views.success, name='success'),
    path('payment', views.payment, name='payment'),

]