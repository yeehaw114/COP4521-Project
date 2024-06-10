from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Workouts, Sets, User_Workouts, User_Sets
from .serializers import WorkoutsSerializer, SetsSerializer, UserWorkoutsSerializer, UserSetsSerializer
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

@permission_classes([IsAuthenticated])
@csrf_protect
@login_required
class WorkoutsViewSet(viewsets.ModelViewSet):
    queryset = Workouts.objects.all()
    serializer_class = WorkoutsSerializer

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)