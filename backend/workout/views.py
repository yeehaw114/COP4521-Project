from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Workout
from .serializers import WorkoutSerializer
from django.contrib.auth.decorators import login_required