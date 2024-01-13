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
class Product(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    product_photo = models.ImageField(upload_to='product_photos/')
    product_name = models.CharField(max_length=100)
    quantity_available = models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='farmer_orders')  # Specify related_name

    def __str__(self):
        return self.product_name


# farmers/models.py
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_ordered = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Update product quantity and delete if quantity is finished
        self.product.quantity_available -= self.quantity_ordered
        if self.product.quantity_available <= 0:
            self.product.delete()
        else:
            self.product.save()
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.product_name} - {self.quantity_ordered}"
