from django.db import models

# Create your models here.




class FarmerPost(models.Model):
    image = models.ImageField(upload_to='farmer_posts/', default='path/to/default-image.jpg')
    title = models.CharField(max_length=255, default='Default Title')
    farm_name = models.CharField(max_length=255, default='Default Farm')
    quantity = models.CharField(max_length=50, default='Default Quantity')
    price = models.CharField(max_length=50, default='Default Price')
    location = models.CharField(max_length=50, default='Default Price')  
    # location = models.PointField(null=True, blank=True)  # Assuming you want to store the location

    def __str__(self):
        return self.title
