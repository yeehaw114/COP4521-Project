from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, RegisterSerializer
from django.middleware.csrf import get_token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie

@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
@csrf_protect
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        login(request, user)
        session_id = request.session.session_key
        csrf_token = get_token(request)
        return Response({'message': 'User created successfully', 'session_id': session_id, 'csrf_token': csrf_token}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
@csrf_protect
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        session_id = request.session.session_key
        csrf_token = get_token(request)
        return Response({'user': UserSerializer(user).data, 'session_id': session_id, 'csrf_token': csrf_token}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@ensure_csrf_cookie
@csrf_protect
def logout_view(request):
    logout(request)
    csrf_token = get_token(request)
    return Response({'message': 'Logged out successfully', 'csrf_token': csrf_token}, status=status.HTTP_200_OK)
