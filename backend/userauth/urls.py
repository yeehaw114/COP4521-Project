from django.urls import path
from .views import login_view, logout_view, register_view, get_csrf_token

urlpatterns = [
    path('auth/csrf-token', get_csrf_token),
    path('auth/login', login_view),
    path('auth/logout', logout_view),
    path('auth/register', register_view),
]