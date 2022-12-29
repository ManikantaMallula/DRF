from django.urls import path
from . import views
urlpatterns=[
    path('homefun/',views.home,name='homefun'),
    path('homecl/',views.HomeView.as_view(),name='homecl'),
    path('aboutfun/', views.aboutfun, name='aboutfun'),
    path('aboutcl/', views.AboutClassView.as_view(), name='aboutcl'),
    path('contactfun/', views.contactfun, name='contactfun'),
    path('contactcl/', views.ContactView.as_view(), name='contactcl'),
    #path('newsfun/', views.newsfun, name='newsfun'),
    path('newsfun/', views.newsfun, {'template_name':'news.html'}, name='newsfun'),
    path('newsfun1/', views.newsfun, {'template_name':'news1.html'}, name='newsfun1'),
    #path('newscl/', views.NewsClassView.as_view(), name='newscl'),
    path('newscl/', views.NewsClassView.as_view(template_name='news.html'), name='newscl'),
    path('newscl1/', views.NewsClassView.as_view(template_name='news1.html'), name='newscl1')
]