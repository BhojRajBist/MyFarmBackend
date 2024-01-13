from django.db import models

# Create your models here.





class Farmer(models.Model):
    uname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    country = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    password = models.CharField(max_length=50)


class Product(models.Model):
    # Assuming Product is associated with a Farmer
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()



class Order(models.Model):
    # Assuming Order is associated with a Product and a Farmer
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    