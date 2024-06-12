from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Workouts, Sets, User_Workouts, User_Sets
from .serializers import WorkoutsSerializer, SetsSerializer, UserWorkoutsSerializer, UserSetsSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workouts.objects.all()
    serializer_class = WorkoutsSerializer
    permission_classes = [IsAuthenticated]

class SetViewSet(viewsets.ModelViewSet):
    queryset = Sets.objects.all()
    serializer_class = SetsSerializer
    permission_classes = [IsAuthenticated]

class UserWorkoutViewSet(viewsets.ModelViewSet):
    queryset = User_Workouts.objects.all()
    serializer_class = UserWorkoutsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

class UserSetViewSet(viewsets.ModelViewSet):
    queryset = User_Sets.objects.all()
    serializer_class = UserSetsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)
