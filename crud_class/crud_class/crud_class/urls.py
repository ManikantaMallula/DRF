"""crud_class URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('crud_class/', include('crud_class.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/',views.ulogin,name='login'),
    path('signup/',views.signup,name='signup'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/', views.Logout, name='logout'),
    path('delete/<int:id>/', views.DeleteView.as_view(),name='delete'),
    path('edit/<int:id>/', views.EditView.as_view(),name='edit'),
    path('/set',views.set_Blog_cookies,name='set'),
    path('/get',views.get_Blog_coookies,name='get'),
    path('/del',views.del_Blog_cookies,name='del'),
    path('/session',views.set_Blog_session,name='session'),
    path('/get_session',views.get_Blog_session,name='get_session'),
    path('/del_session', views.del_Blog_session, name='del_session'),
    path('/excep',views.excep,name='excep'),
    path('/user',views.user,name='user'),
    #path('mid',views.middleware),
]
