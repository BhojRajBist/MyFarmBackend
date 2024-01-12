# api/urls.py

from django.urls import path
from .views import FarmerPostList

urlpatterns = [
     path('farmer-posts/', FarmerPostList.as_view(), name='farmer-post-list'),
]
