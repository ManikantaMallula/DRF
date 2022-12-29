from django.urls import path
from django.contrib import admin
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show, name="addandshow"),
    path('delete/<int:id>/', views.delete, name="deletedata"),
    path('<int:id>/', views.edit, name="updatedata"),
    path("sign",views.signup,name="signup"),
    path('profile',views.userprofile,name="profile"),
    path('login/',views.userlogin,name='login'),
]