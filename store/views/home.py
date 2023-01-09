from django.http import HttpResponse
from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


class Index(View):
    def get(self, request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        categories = Category.get_all_categories()
        # catt = request.GET['category']
        # if catt:
        #     products = Product.sort_by_categories(catt)
        val = request.GET.get('category')
        if val:
            products = Product.sort_by_categories(val)
        else:
            products = Product.get_all_products()
        data = {'products': products, 'categories': categories}
        print(request.session.get('user_name'))
        return render(request, 'index.html', data)

    def post(self, request):
        data = request.POST
        product = data.get('product')
        remove = request.POST.get('deduct')

        cart = request.session.get('cart')
        if cart:
            exist_in_cart = cart.get(product)
            if exist_in_cart:
                if remove:
                    if exist_in_cart <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = exist_in_cart - 1
                else:
                    cart[product] = exist_in_cart + 1
            else:
                cart[product] = 1
        else:
            cart = {product: 1}

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('homepage')
