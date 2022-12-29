from django.urls import path
from . import views

urlpatterns = [
    #path('', views.TemplateView.as_view(template_name='home.html'), name='home'),
    path('index/', views.TemplateView.as_view(template_name='home.html'), name='index'),

    #path('', views.HomeTemplateView.as_view(), name='home'),

    path('', views.HomeTemplateView.as_view(extra_context={'course':'Python'}), name='home'),
    #path('home/<int:cl>/', views.HomeTemplateView.as_view(), name='cl')
]
