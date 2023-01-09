from django.shortcuts import render, redirect
from django.views import View

from store.models.product import Product
from store.models.orders import Order

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart'))
        result = Product.get_product_by_id(ids)
        
        return render(request, 'cart.html', {'cart_prod': result})
        
    
        
        
