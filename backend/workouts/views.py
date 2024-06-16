from django.db import transaction
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
        return Response(status=status.HTTP_200_OK)
    
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
        return Response(status=status.HTTP_200_OK)
    
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
        return Response(status=status.HTTP_200_OK)
    
class WorkoutsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post', 'delete']
    serializer_class = WorkoutsSerializer
    queryset = Workouts.objects.all()

    def get_queryset(self):
        return self.queryset.filter(username=self.request.user)
    
    def perform_create(self, serializer):
        sets_data = serializer.validated_data.pop('sets', [])
        request_user = self.request.user
        
        with transaction.atomic():
            workout = Workouts.objects.create(username=request_user, **serializer.validated_data)
            for set_data in sets_data:
                Sets.objects.create(workout_id=workout, **set_data)

    @action(detail=True, methods=['get'], url_path='details')
    def workout_details(self, request, pk=None):
        workout = self.get_object()
        sets = Sets.objects.filter(workout_id=workout)
        workout.sets = sets
        serializer = self.get_serializer(workout)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def all(self, request):
        queryset = self.queryset.filter(username=self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['delete'])
    def clear(self, request):
        queryset = self.queryset.filter(username=self.request.user)
        queryset.delete()
        return Response(status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['delete'], url_path='delete')
    def delete_workout(self, request, pk=None):
        workout = self.get_object()
        with transaction.atomic():
            Sets.objects.filter(workout_id=workout).delete()
            workout.delete()
        return Response(status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'], url_path='log')
    def log_workout(self, request, pk=None):
        workout_id = pk
        user = request.user
        data = request.data

        try:
            user_workout = User_Workouts.objects.create(workout_id_id=workout_id, username=user)

            sets = data.get('sets', [])
            for set_data in sets:
                exercise = set_data.get('exercise')
                reps = set_data.get('reps')
                weight = set_data.get('weight')

                set_instance, created = Sets.objects.get_or_create(workout_id=workout_id, exercise=exercise, defaults={'reps': reps, 'weight': weight})
                User_Sets.objects.create(user_workout_id=user_workout, set_id=set_instance, reps=reps, weight=weight, username=user)

            return Response({'message': 'Workout logged successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)