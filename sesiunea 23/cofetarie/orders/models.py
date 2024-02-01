from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def total_price(self):
        return self.quantity * self.product.price


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def total_price(self):
        return sum([item.total_price() for item in self.items.iterator()])

    @staticmethod
    def get_curent_order(user):
        qs = Order.objects.filter(user__id=user.id, ordered=False)
        if qs:
            return qs[0]
