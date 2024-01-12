from django.shortcuts import render

# Create your views here.

# api/views.py

from rest_framework import generics
from .models import FarmerPost
from .serializers import FarmerPostSerializer

class FarmerPostList(generics.ListCreateAPIView):
    queryset = FarmerPost.objects.all()
    serializer_class = FarmerPostSerializer

class FarmerPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FarmerPost.objects.all()
    serializer_class = FarmerPostSerializer
