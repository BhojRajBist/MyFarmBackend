# # buyer/signals.py
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Order
# from farmer.models import Product

# @receiver(post_save, sender=Order)
# def update_product_quantity(sender, instance, created, **kwargs):
#     if created:
#         product = instance.product
#         product.quantity_available -= instance.quantity_ordered
#         product.save()
