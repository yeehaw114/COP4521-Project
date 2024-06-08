from django.urls import path
from .views import login_view, logout_view, register_view

urlpatterns = [
    path('api/login', login_view),
    path('api/logout', logout_view),
    path('api/register', register_view),
]