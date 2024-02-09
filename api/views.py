from django.shortcuts import render
from django.http import JsonResponse
from api.models import User

from api.serializer import MyTokenObtainPairSerializer, RegisterSerializer,PasswordResetSerializer,QuizResultSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView

# views.py for Resetpassword
from rest_framework import generics, status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .models import PasswordReset
from .serializer import PasswordResetSerializer



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# Get All Routes

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/password-reset/',
        '/api/token/refresh/',
        'api/make-payment/'
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = "Hello buddy"
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)


import secrets

def generate_unique_token():
    return secrets.token_urlsafe(32) 


def send_password_reset_email(email, reset_link):
    subject = 'Password Reset Request'
    message = f'Click the following link to reset your password: {reset_link}'
    from_email = 'bhojbist2020@gmail.com'  # Update with your email address
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)

User = get_user_model()

class PasswordResetRequestView(generics.CreateAPIView):
    serializer_class = PasswordResetSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        user = User.objects.filter(email=email).first()

        if user:
            # Generate a unique token (you can use a library like `secrets` for this)
            token = generate_unique_token()

            # Create a PasswordReset entry
            PasswordReset.objects.create(user=user, token=token)

            # Send an email with the reset link
            reset_link = f"https://ab.geoneer.com.np/reset-password?token={token}"
            send_password_reset_email(email, reset_link)

            return Response(
                {"message": "If the email exists, a password reset link has been sent to your email."},
                status=status.HTTP_200_OK
            )

        return Response(
            {"message": "No user with that email address exists."},
            status=status.HTTP_400_BAD_REQUEST
        )

# import uuid 
# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     uid =uuid.uuid4()
#     context["uid"] =uid
#     print ('uid',uid) 
#     return context

    
# views.py
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests

@csrf_exempt
def make_payment(request):
    if request.method == 'POST':
        # Extract payment data from the request
        payment_data = {
            'tAmt': request.POST.get('tAmt'),
            'amt': request.POST.get('amt'),
            'txAmt': request.POST.get('txAmt'),
            'psc': request.POST.get('psc'),
            'pdc': request.POST.get('pdc'),
            'scd': request.POST.get('scd'),
            'pid': request.POST.get('pid'),
            'su': request.POST.get('su'),
            'fu': request.POST.get('fu'),
        }

        # Make a request to eSewa API
        esewa_response = requests.post('https://uat.esewa.com.np/epay/main', data=payment_data)
        print(esewa_response.text)

        # Process eSewa response and redirect the user
        # You may need to parse the eSewa response and handle the redirection accordingly
        # For example, you can check the 'Success' parameter in the response

        # Assuming eSewa returns a JSON response
        esewa_response_json = esewa_response.json()

        if esewa_response_json.get('Success') == 'True':
            return redirect(payment_data['su'])
        else:
            return redirect(payment_data['fu'])

    return JsonResponse({'error': 'Invalid request method'})

from rest_framework import generics
from rest_framework.response import Response
from .models import QuizResult
from .serializer import QuizResultSerializer
 

class QuizResultListCreateView(generics.ListCreateAPIView):
    queryset = QuizResult.objects.all()
    serializer_class = QuizResultSerializer

    def list(self, request, *args, **kwargs):
        # Customizing the list method to return a response with additional information
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response_data = {
            'count': queryset.count(),
            'results': serializer.data,
        }
        return Response(response_data)

    def create(self, request, *args, **kwargs):
        # Customizing the create method to handle quiz result submission
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response_data = {
            'message': 'Quiz result submitted successfully.',
            'result': serializer.data,
        }
        return Response(response_data)

