# # farmers/views.py
# from rest_framework import generics
# from rest_framework.response import Response
# from .models import Farmer, Product, Order
# from .serializers import FarmerSerializer, ProductSerializer, OrderSerializer

# class FarmerListCreateView(generics.ListCreateAPIView):
#     queryset = Farmer.objects.all()
#     serializer_class = FarmerSerializer

# class ProductListCreateView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# # class OrderListCreateView(generics.ListCreateAPIView):
# #     queryset = Order.objects.all()
# #     serializer_class = OrderSerializer
    

# class OrderListCreateView(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     def create(self, request, *args, **kwargs):
#         product_id = request.data.get('product')
#         quantity_ordered = request.data.get('quantity_ordered')
#         buyer_name = request.data.get('buyer_name')

#         try:
#             product = Product.objects.get(pk=product_id)
#         except Product.DoesNotExist:
#             return Response({"error": "Product not found"}, status=404)

#         order = product.place_order(quantity_ordered, buyer_name)

#         if order:
#             serializer = self.get_serializer(order)
#             headers = self.get_success_headers(serializer.data)
#             return Response(serializer.data, status=201, headers=headers)
#         else:
#             return Response({"error": "Insufficient quantity available"}, status=400)


# farmers/views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Farmer, Product, Order
from .serializers import FarmerSerializer, ProductSerializer, OrderSerializer

@api_view(['POST'])
def signup_farmer(request):
    serializer = FarmerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
