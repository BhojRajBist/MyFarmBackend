# buyer/models.py
from django.db import models
from farmer.models import Product

class Buyer(models.Model):
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey('farmer.Product', on_delete=models.CASCADE, related_name='buyer_orders')  # Specify related_name
    quantity_ordered = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.buyer.name}'s order for {self.quantity_ordered} units of {self.product.product_name}"