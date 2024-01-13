# buyer/views.py
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Buyer, Order
from .serializers import OrderSerializer
from rest_framework import generics

class BuyerListView(ListView):
    model = Buyer
    template_name = 'buyer/buyer_list.html'

class OrderCreateView(CreateView):
    model = Order
    template_name = 'buyer/order_form.html'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.buyer = Buyer.objects.get(id=self.kwargs['buyer_id'])
        return super().form_valid(form)

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
