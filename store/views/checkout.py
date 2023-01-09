from django.shortcuts import render, redirect
from django.views import View

from store.models.product import Product
from store.models.user import User
from store.models.orders import Order


class Checkout(View):
    def post(self, request):
        data = request.POST
        address = data.get('address')
        phone = data.get('phone')
        user = request.session.get('user_id')
        cart = request.session.get('cart')
        product = Product.get_product_by_id(list(cart.keys()))
        for i in product:
            print(cart.get(str(i.id)))
            neworder = Order(
                user=User(id=user),
                product=i,
                quantity=cart.get(str(i.id)),
                price=i.price,
                address=address,
                phone=phone
            )

            neworder.save()
            request.session['cart']={}

        return redirect('cart')
