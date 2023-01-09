from django.shortcuts import render, redirect
from django.views import View

from store.models.product import Product
from store.models.orders import Order

class Myorders(View):
    def get(self, request):
        ids = request.session.get('user_id')

        result = list(Order.get_order_by_id(ids))
        return render(request, 'myorders.html', {'my_orders': result})
        
    
        
        
