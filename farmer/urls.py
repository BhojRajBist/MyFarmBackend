# api/urls.py

from django.urls import path
from .views import FarmerPostList, FarmerPostDetail

urlpatterns = [
    path('farmer-posts/', FarmerPostList.as_view(), name='farmer-post-list'),
    path('farmer-posts/<int:pk>/', FarmerPostDetail.as_view(), name='farmer-post-detail'),
]
