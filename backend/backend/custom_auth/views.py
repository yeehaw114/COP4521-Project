from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework.decorators import action
from backend.custom_auth.serializers import LoginSerializer, RegisterSerializer
from backend.user.models import User

class RegistrationViewSet(ModelViewSet, TokenObtainPairView):
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        res = {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": serializer.data,
        }

        return Response(res, status=status.HTTP_201_CREATED)

class LoginViewSet(ModelViewSet, TokenObtainPairView):
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class RefreshViewSet(viewsets.ViewSet, TokenRefreshView):
    persmission_classes = (AllowAny,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        
        data = serializer.validated_data

        refresh_token = request.data.get('refresh')
        refresh = RefreshToken(refresh_token)
        user_id = refresh['user_id']
        user = User.objects.get(id=user_id)

        data['username'] = user.username

        return Response(data, status=status.HTTP_200_OK)
    
class TokenViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['get'])
    def validate_token(self, request):
        return Response({"username": request.user.username}, status=status.HTTP_200_OK)