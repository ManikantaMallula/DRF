from django.urls import path
from app import views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('profile/', login_required(views.Profile.as_view()), name='profile'),
    path('home/', staff_member_required(views.Profile.as_view()), name='home'),

]