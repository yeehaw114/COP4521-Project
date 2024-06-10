from rest_framework import serializers
from .models import Workouts, Sets, User_Workouts, User_Sets

class WorkoutsSerializer(serializers.ModelSerializer):
    model = Workouts
    fields = ['id', 'name', 'username']

class SetsSerializer(serializers.ModelSerializer):
    model = Sets
    fields = ['id', 'workout_id', 'exercise', 'reps', 'weight']

class UserWorkoutsSerializer(serializers.ModelSerializer):
    model = User_Workouts
    fields = ['id', 'workout_id', 'username', 'done_date']

class UserSetsSerializer(serializers.ModelSerializer):
    model = User_Sets
    fields = ['id', 'user_workout_id', 'set_id', 'reps', 'weight', 'username']