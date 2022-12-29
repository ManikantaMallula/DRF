from django.urls import path
from . import views
urlpatterns = [
    path('', views.TemplateView.as_view(template_name='home.html'), name='blankhome'),
    path('home/', views.RedirectView.as_view(url='/'), name='abc'),
    path('index/', views.RedirectView.as_view(url='/'), name='index'),
    path('index/', views.RedirectView.as_view(pattern_name='abc'), name='index'),
    path('g/', views.RedirectView.as_view(url='https://www.google.com/'), name='google'),
    path('g1/', views.ojasRedirectView.as_view(), name='google'),

    path('home/<int:pk>/', views.newRedirectView.as_view(), name='geek'),
    path('<int:pk>/', views.TemplateView.as_view(template_name='home.html'), name='mindex'),

    path('home/<slug:post>/', views.newRedirectView.as_view()),
    path('<slug:post>/', views.TemplateView.as_view(template_name='home.html'), name='mindex'),
]

