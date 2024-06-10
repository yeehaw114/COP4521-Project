from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Workout
from .serializers import WorkoutSerializer
from django.contrib.auth.decorators import login_required

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@login_required
def create_workout(request):
    user = request.user
    data = request.data.copy()
    data['username'] = user.username
    serializer = WorkoutSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
