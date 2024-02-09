from django.urls import path
from . import views
from .views import PasswordResetRequestView
from .views import QuizResultListCreateView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', views.testEndPoint, name='test'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    # path('api/make-payment/', make_payment, name='make_payment'),
    path('api/quiz-results/', QuizResultListCreateView.as_view(), name='quiz-results'),
    path('', views.getRoutes),
    
]

