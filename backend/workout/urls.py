from django.urls import path
from .views import create_workout

urlpatterns = [
    path('api/create_workout', create_workout, name='create_workout'),
]