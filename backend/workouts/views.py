from django.db import transaction
import logging
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from workouts.models import Workouts, Sets, User_Workouts, User_Sets
from workouts.serializers import WorkoutsSerializer, SetsSerializer, UserWorkoutsSerializer, UserSetsSerializer
from django.http import JsonResponse
from django.db import connection

logger = logging.getLogger(__name__)

class UserSetsViewSet(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthenticatedOrReadOnly,)
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
    permission_classes = (IsAuthenticatedOrReadOnly,)
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
    
    @action(detail=False, methods=['get'], url_path='logs')
    def user_workout_logs(self, request):
        user = request.user
        user_workouts = User_Workouts.objects.filter(username=user)
        serializer = UserWorkoutsSerializer(user_workouts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
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
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = WorkoutsSerializer
    queryset = Workouts.objects.all()

    def get_queryset(self):
        logger.debug(self)
        return self.queryset
    
    def perform_create(self, serializer):
        sets_data = serializer.validated_data.pop('sets', [])
        request_user = self.request.user
        
        with transaction.atomic():
            workout = Workouts.objects.create(username=request_user, **serializer.validated_data)
            for set_data in sets_data:
                Sets.objects.create(workout_id=workout, **set_data)

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

    @action(detail=True, methods=['get'], url_path='details')
    def workout_details(self, request, pk=None):
        workout = self.get_object()
        sets = Sets.objects.filter(workout_id=workout)
        workout.sets = sets
        serializer = self.get_serializer(workout)
        return Response(serializer.data)
    
    @action(detail=True, methods=['delete'], url_path='delete')
    def delete_workout(self, request, pk=None):
        workout = self.get_object()
        with transaction.atomic():
            Sets.objects.filter(workout_id=workout).delete()
            workout.delete()
        return Response(status=status.HTTP_200_OK)
    

    @action(detail=True, methods=['post'], url_path='log-workout')
    def log_workout(self, request, pk=None):
        workout_id = pk
        user = request.user
        data = request.data

        try:
            with transaction.atomic():
                user_workout = User_Workouts.objects.create(workout_id_id=workout_id, username=user)

                sets = data.get('sets', [])
                for set_data in sets:
                    User_Sets.objects.create(
                        user_workout_id=user_workout,
                        username=user,
                        exercise=set_data.get('exercise'),
                        reps=set_data.get('reps'),
                        weight=set_data.get('weight')
                    )

            return Response({'message': 'Workout logged successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['get'], url_path='log')
    def get_log(self, request, pk=None):
        log_id = pk
        user = request.user

        try:
            user_workout = User_Workouts.objects.get(id=log_id, username=user)
            
            user_sets = User_Sets.objects.filter(user_workout_id=user_workout)
            serializer = UserSetsSerializer(user_sets, many=True)

            workout_data = {
                "name": user_workout.workout_id.name,
                "done_date": user_workout.done_date,
                "sets": serializer.data
            }

            return Response(workout_data, status=status.HTTP_200_OK)
        except User_Workouts.DoesNotExist:
            return Response({'error': 'User workout log not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'], url_path='delete-log')
    def delete_log(self, request, pk=None):
        log_id = pk
        user = request.user

        try:
            user_workout = User_Workouts.objects.get(id=log_id, username=user)
            
            with transaction.atomic():
                User_Sets.objects.filter(user_workout_id=user_workout).delete()
                user_workout.delete()

            return Response({'message': 'User workout log deleted successfully'}, status=status.HTTP_200_OK)
        except User_Workouts.DoesNotExist:
            return Response({'error': 'User workout log not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['put'], url_path='update-log')
    def update_log(self, request, pk=None):
        try:
            user_workout = User_Workouts.objects.get(pk=pk, username=request.user)
            data = request.data
            sets_data = data.pop('sets', [])

            with transaction.atomic():
                user_workout.done_date = data.get('done_date', user_workout.done_date)
                user_workout.save()

                existing_set_ids = [set_item['id'] for set_item in sets_data if 'id' in set_item]
                User_Sets.objects.filter(user_workout_id=user_workout).exclude(id__in=existing_set_ids).delete()

                for set_data in sets_data:
                    set_id = set_data.get('id')
                    if set_id:
                        set_instance = User_Sets.objects.get(id=set_id, user_workout_id=user_workout)
                        set_instance.exercise = set_data.get('exercise', set_instance.exercise)
                        set_instance.reps = set_data.get('reps', set_instance.reps)
                        set_instance.weight = set_data.get('weight', set_instance.weight)
                        set_instance.save()
                    else:
                        User_Sets.objects.create(
                            user_workout_id=user_workout,
                            username=request.user,
                            exercise=set_data.get('exercise'),
                            reps=set_data.get('reps'),
                            weight=set_data.get('weight')
                        )
                    
                serializer = UserWorkoutsSerializer(user_workout)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except User_Workouts.DoesNotExist:
            return Response({'error': 'User workout log not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'], url_path='user-templates')
    def user_workouts(self, request):
        user = request.user
        workouts = Workouts.objects.filter(username=user)
        serializer = WorkoutsSerializer(workouts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'], url_path='all-templates')
    def all_templates(self, request):
        workouts = Workouts.objects.all()
        serializer = WorkoutsSerializer(workouts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)