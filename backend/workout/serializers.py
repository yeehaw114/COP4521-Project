from rest_framework import serializers
from .models import Workout, Workout_Exercises, Exercise, User_Workouts, User_Sets

class WorkoutSerializer(serializers.ModelSerializer):
    model = Workout
    fields = ['id', 'name', 'username']

class ExerciseSerializer(serializers.ModelSerializer):
    model = Exercise
    fields = ['id', 'name', 'muscle_group']

class WorkoutExercisesSerializer(serializers.ModelSerializer):
    model = Workout_Exercises
    fields = ['id', 'workout_id', 'exercise_name', 'reps', 'weight']

class UserWorkoutsSerializer(serializers.ModelSerializer):
    model = User_Workouts
    fields = ['id', 'workout_id', 'username', 'done_date']

class UserSetsSerializer(serializers.ModelSerializer):
    model = User_Sets
    fields = ['id', 'user_workout_id', 'reps', 'weight', 'username']