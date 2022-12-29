from django.shortcuts import render
from .models import Customer, Category, Product, Cart, Cartitem
from django.views.generic import TemplateView, View


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Alex'
        context['product_list'] = Product.objects.all()
        return context

class Productdetails(TemplateView):
    template_name = 'details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs["slug"]
        #print(slug)
        product = Product.objects.get(slug=url_slug)
        context[product]=product
        return context

class Cart(TemplateView):
    template_name = 'cart.html'


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        product_id = self.kwargs['pro_id']                  #get product id from requested url
        product_obj = Product.objects.get(id=product_id)    #get product
        cart_id=self.request.session.get('cart_id',None)

        # check if product already exists in cart
        if cart_id:
            cart_obj = Cart.objects.ger(id=cart_id)
            this_product_in_cart = cart_obj.Cart_set.filter(product=product_obj)

            if this_product_in_cart.exists():
                cartproduct = this_product_in_cart.last()
                cartproduct.quantity += 1
                cartproduct.subtotal += product_obj.selling_price
                cartproduct.save()
                cart_obj.total += product_obj.selling_price
                cart_obj.save()

            else:
                cartproduct = Cart.objects.create(cart=cart_obj, product=product_obj, rate=product_obj.selling_price,
                                                         quantity=1,subtotal=product_obj.selling_price)
                cart_obj.total += product_obj.selling_price
                cart_obj.save()





        else:
            cart_obj = Cart.objects.create(total=o)
            self.request.session['cart_id'] = cart_obj.id
            cartproduct = Cart.objects.create(cart=cart_obj, product=product_obj, rate=product_obj.selling_price,
                                                     quantity=1,subtotal=product_obj.selling_price)
            cart_obj.total += product_obj.selling_price
            cart_obj.save()

        return context








class CartView(TemplateView):
    template_name = 'cartpage.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        cart_id=self.request.session.get('cart_id',None)
        if cart_id:
            cart=Cart.objects.get(id=cart_id)
        else:
            cart=None
        context['cart']=cart
        return context

