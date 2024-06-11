from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Workouts, Sets, User_Workouts, User_Sets
from .serializers import WorkoutSerializer, SetSerializer, UserWorkoutSerializer, UserSetSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workouts.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]

class SetViewSet(viewsets.ModelViewSet):
    queryset = Sets.objects.all()
    serializer_class = SetSerializer
    permission_classes = [IsAuthenticated]

class UserWorkoutViewSet(viewsets.ModelViewSet):
    queryset = User_Workouts.objects.all()
    serializer_class = UserWorkoutSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

class UserSetViewSet(viewsets.ModelViewSet):
    queryset = User_Sets.objects.all()
    serializer_class = UserSetSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)
