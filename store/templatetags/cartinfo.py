from django import template

register = template.Library()


@register.filter(name='check_appearance')
def check_appearance(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            print(id)
            return cart.get(id)
    return False


@register.filter(name='cart_count')
def cart_count(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0


@register.filter(name='product_price')
def product_price(product, cart):
    return product.price * cart_count(product, cart)


@register.filter(name='total_price')
def total_price(products, cart):
    sum = 0
    for p in products:
        sum += product_price(p, cart)
    return sum

@register.filter(name='total_products')
def total_products(products,cart):
    return len(cart)
