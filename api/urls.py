from django.urls import path
from api.views import SendPasswordResetEmailView,  UserActivationView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserPasswordResetView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('activate/<uid>/<token>/', UserActivationView.as_view(), name='activate'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),

]
