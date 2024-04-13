# # buyer/views.py
# from django.shortcuts import render
# from django.views.generic import ListView, CreateView
# from .models import Buyer, Order
# from .serializers import OrderSerializer
# from rest_framework import generics

# class BuyerListView(ListView):
#     model = Buyer
#     template_name = 'buyer/buyer_list.html'

# class OrderCreateView(CreateView):
#     model = Order
#     template_name = 'buyer/order_form.html'
#     fields = '__all__'

#     def form_valid(self, form):
#         form.instance.buyer = Buyer.objects.get(id=self.kwargs['buyer_id'])
#         return super().form_valid(form)

# class OrderListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

# buyers/views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Buyer, Order
from .serializers import BuyerSerializer, OrderSerializer

@api_view(['POST'])
def signup_buyer(request):
    serializer = BuyerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

