from django.db import models

# Create your models here.
# api/models.py
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_farmer = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    # Add related_name attributes to avoid clash with auth.User model
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')

    def __str__(self):
        return self.username
