from django.db import models

# Create your models here.


class FarmerPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title