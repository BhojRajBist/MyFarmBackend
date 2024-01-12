# api/serializers.py

from rest_framework import serializers
from .models import FarmerPost

class FarmerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerPost
        fields = ['id', 'title', 'content', 'price', 'location']
