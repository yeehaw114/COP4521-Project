from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Workout, Exercise, Workout_Exercises, User_Workouts, User_Sets
from .serializers import WorkoutSerializer, ExerciseSerializer, WorkoutExercisesSerializer, UserWorkoutsSerializer, UserSetsSerializer
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

@permission_classes([IsAuthenticated])
@csrf_protect
@login_required
class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

@permission_classes([IsAuthenticated])
@csrf_protect
@login_required
class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

@permission_classes([IsAuthenticated])
@csrf_protect
@login_required
class WorkoutExercisesViewSet(viewsets.ModelViewSet):
    queryset = Workout_Exercises.objects.all()
    serializer_class = WorkoutExercisesSerializer

    def perform_create(self, serializer):
        serializer.save(workout_id=self.request.data['workout_id'], exercise_name=self.request.data['exercise_name'])
