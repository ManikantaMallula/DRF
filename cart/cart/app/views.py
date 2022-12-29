from django.shortcuts import render
from .models import Product, Cart_items


def home(request):
    model = Product.objects.all
    return render(request, 'home.html', {'model':model})


def addcart(request):
    print(request.POST['prod_id'])
    request.session.get['cart'] = {}
    for k,v in request.session.get['cart'].items():
        print(k,v)



    return render(request, 'cart.html')

def details(request):
    pass