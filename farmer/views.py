from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListCreateAPIView
from .models import FarmerPost
from .serializers import FarmerPostSerializer

class FarmerPostList(ListCreateAPIView):
    queryset = FarmerPost.objects.all()
    serializer_class = FarmerPostSerializer
