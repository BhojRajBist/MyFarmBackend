# # buyer/serializers.py
# from rest_framework import serializers
# from .models import Order

# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = '__all__'

# buyers/serializers.py

from rest_framework import serializers
from .models import Buyer, Order

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

