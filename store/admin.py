from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.user import User
from .models.orders import Order

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminUser(admin.ModelAdmin):
    list_display = ['uname', 'uemail', 'uaddress', 'ugender', 'upassword', 'condition']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(User, AdminUser)
admin.site.register(Order)