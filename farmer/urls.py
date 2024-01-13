# farmers/urls.py
from django.urls import path
from .views import FarmerListCreateView, ProductListCreateView, OrderListCreateView

urlpatterns = [
    path('farmers/', FarmerListCreateView.as_view(), name='farmer-list-create'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
]
