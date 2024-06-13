from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from workouts.models import Workouts, Sets, User_Workouts, User_Sets
from workouts.serializers import WorkoutsSerializer, SetsSerializer, UserWorkoutsSerializer, UserSetsSerializer

class UserSetsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post', 'delete']
    serializer_class = UserSetsSerializer
    queryset = User_Sets.objects.all()

    def get_queryset(self):
        return self.queryset.filter(username=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(username=self.request.user)
    
    @action(detail=False, methods=['get'])
    def all(self, request):
        queryset = self.queryset.filter(username=self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['delete'])
    def clear(self, request):
        queryset = self.queryset.filter(username=self.request.user)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserWorkoutsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post', 'delete']
    serializer_class = UserWorkoutsSerializer
    queryset = User_Workouts.objects.all()

    def get_queryset(self):
        return self.queryset.filter(username=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(username=self.request.user)
    
    @action(detail=False, methods=['get'])
    def all(self, request):
        queryset = self.queryset.filter(username=self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['delete'])
    def clear(self, request):
        queryset = self.queryset.filter(username=self.request.user)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SetsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post', 'delete']
    serializer_class = SetsSerializer
    queryset = Sets.objects.all()

    def get_queryset(self):
        return self.queryset.filter(workout_id=self.kwargs['workout_id'])
    
    @action(detail=False, methods=['get'])
    def all(self, request, workout_id=None):
        queryset = self.queryset.filter(workout_id=workout_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['delete'])
    def clear(self, request, workout_id=None):
        queryset = self.queryset.filter(workout_id=workout_id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class WorkoutsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post', 'delete']
    serializer_class = WorkoutsSerializer
    queryset = Workouts.objects.all()

    def get_queryset(self):
        return self.queryset.filter(username=self.request.user)
    
    @action(detail=False, methods=['get'])
    def all(self, request):
        queryset = self.queryset.filter(username=self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['delete'])
    def clear(self, request):
        queryset = self.queryset.filter(username=self.request.user)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

