from rest_framework.routers import SimpleRouter
from django.urls import path, include

from auth.views import LoginViewSet, RegistrationViewSet, RefreshViewSet, TokenViewSet

auth_router = SimpleRouter()

auth_router.register(r'auth/login', LoginViewSet, basename='auth-login')
auth_router.register(r'auth/register', RegistrationViewSet, basename='auth-register')
auth_router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

urlpatterns = [
    path('', include(auth_router.urls)),
    path('auth/login/token', TokenViewSet.as_view({'get': 'validate_token'}), name='token_validate'),
]