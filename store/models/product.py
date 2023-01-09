from django.db import models
from django.db.models import Q

from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50, default='')
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def sort_by_categories(catid):
        if catid:
            print(catid)
            return Product.objects.filter(category_id=catid)
        else:
            return Product.get_all_products()
