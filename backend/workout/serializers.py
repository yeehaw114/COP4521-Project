from rest_framework import serializers
from .models import Workout, Workout_Exercises, Exercise

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['name', 'muscle_group']

class WorkoutExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout_Exercises
        fields = ['workout_id', 'exercise_name', 'reps', 'weight']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'name', 'username']