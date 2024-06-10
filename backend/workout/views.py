from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import WorkoutSerializer, ExerciseSerializer, WorkoutExercisesSerializer
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@csrf_protect
@login_required
def create_workout(request):
    user = request.user
    data = request.data.copy()
    data['username'] = user.id
    workout_name = request.data.get('name')
    exercise_name = request.data.get('exercise_name')
    reps = request.data.get('reps')
    weight = request.data.get('weight')
    muscle_group = request.data.get('muscle_group')

    exercise_serializer = ExerciseSerializer(data={'name': exercise_name, 'muscle_group': muscle_group})
    if exercise_serializer.is_valid():
        exercise_instance = exercise_serializer.save()
    else:
        return Response(exercise_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    workout_serializer = WorkoutSerializer(data={'name': workout_name, 'username_id': user})
    if workout_serializer.is_valid():
        workout_instance = workout_serializer.save()
    else:
        return Response(workout_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    workout_exercises_serializer = WorkoutExercisesSerializer(data={
            'workout_id': workout_instance.id,
            'exercise_name': exercise_instance.name,
            'reps': reps,
            'weight': weight
        })
    if workout_exercises_serializer.is_valid():
        workout_exercises_instance = workout_exercises_serializer.save()
    else:
        return Response(workout_exercises_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Workout template created successfully.'}, status=status.HTTP_201_CREATED)
