from django.db import models
from django.db.models import Q
from .product import Product
from .user import User
import datetime

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.IntegerField(default=0)
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)

    def placeorder(self):
        self.save()
    
    @staticmethod
    def get_order_by_id(ids):
        return Order.objects.filter(user_id=ids).order_by('-date')



