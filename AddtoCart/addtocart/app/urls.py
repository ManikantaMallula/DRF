from django.urls import path
from .views import *

urlpatterns = [
    path("", Home.as_view(), name='home'),
    path('product/<slug:slug>/', Productdetails.as_view(), name='details'),
    path('add-to-cart-<int:pro_id>/', Cart.as_view(), name="addtocart"),
    path('mycart/',CartView.as_view(),name='mycart'),

]