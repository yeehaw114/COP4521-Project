from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Workouts, Sets, User_Workouts, User_Sets

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class WorkoutsSerializer(serializers.ModelSerializer):
    username = UserSerializer(read_only=True)

    class Meta:
        model = Workouts
        fields = ['id', 'name', 'username']

class SetsSerializer(serializers.ModelSerializer):
    workout_id = WorkoutsSerializer(read_only=True)

    class Meta:
        model = Sets
        fields = ['id', 'workout_id', 'exercise', 'reps', 'weight']

class UserWorkoutsSerializer(serializers.ModelSerializer):
    workout_id = WorkoutsSerializer(read_only=True)
    username = UserSerializer(read_only=True)

    class Meta:
        model = User_Workouts
        fields = ['id', 'workout_id', 'username', 'done_date']

class UserSetsSerializer(serializers.ModelSerializer):
    user_workout_id = UserWorkoutsSerializer(read_only=True)
    set_id = SetsSerializer(read_only=True)
    username = UserSerializer(read_only=True)

    class Meta:
        model = User_Sets
        fields = ['id', 'user_workout_id', 'set_id', 'reps', 'weight', 'username']