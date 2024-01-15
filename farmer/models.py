# farmers/models.py
from django.db import models


class Farmer(models.Model):
    farm_name = models.CharField(max_length=100)
    email_or_contact = models.CharField(max_length=100)
    farm_type = models.CharField(max_length=50)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.farm_name


# farmers/models.py
# class Product(models.Model):
#     farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
#     product_photo = models.ImageField(upload_to='product_photos/')
#     product_name = models.CharField(max_length=100)
#     quantity_available = models.PositiveIntegerField()
#     price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.product_name
    
class Product(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    product_photo = models.ImageField(upload_to='product_photos/')
    product_name = models.CharField(max_length=100)
    quantity_available = models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    def place_order(self, quantity_ordered, buyer_name):
        if self.quantity_available >= quantity_ordered:
            order = Order.objects.create(product=self, quantity_ordered=quantity_ordered, buyer_name=buyer_name)
            self.quantity_available -= quantity_ordered
            self.save()
            return order
        else:
            return None

from buyer.models import *
# farmers/models.py
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='farmer_orders')
    quantity_ordered = models.PositiveIntegerField()
    buyer_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.buyer_name}'s order for {self.quantity_ordered} units of {self.product.product_name}"

    def get_buyer_name(self):
        return self.buyer_name

    def get_quantity_ordered(self):
        return self.quantity_ordered

