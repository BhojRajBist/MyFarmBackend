# api/serializers.py

# myfarm/api/serializers.py

from rest_framework import serializers
from .models import FarmerPost

class FarmerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerPost
        fields = ('id', 'image', 'title', 'farm_name', 'quantity', 'price', 'location')

