# farmers/views.py
from rest_framework import generics
from .models import Farmer, Product, Order
from .serializers import FarmerSerializer, ProductSerializer, OrderSerializer

class FarmerListCreateView(generics.ListCreateAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
