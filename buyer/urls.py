# buyer/urls.py
from django.urls import path
from .views import BuyerListView, OrderCreateView, OrderListCreateAPIView

urlpatterns = [
    path('buyers/', BuyerListView.as_view(), name='buyer_list'),
    path('buyers/<int:buyer_id>/order/', OrderCreateView.as_view(), name='order_create'),
    path('api/orders/', OrderListCreateAPIView.as_view(), name='order_list_create_api'),
]
