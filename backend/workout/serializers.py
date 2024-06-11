from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Workouts, Sets, User_Workouts, User_Sets

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sets
        fields = ['exercise', 'reps', 'weight']

class WorkoutSerializer(serializers.ModelSerializer):
    sets = SetSerializer(many=True)

    class Meta:
        model = Workouts
        fields = ['id', 'name', 'sets']
        read_only_fields = ['id']

    def create(self, validated_data):
        sets_data = validated_data.pop('sets')
        workout = Workouts.objects.create(**validated_data)
        for set_data in sets_data:
            Sets.objects.create(workout_id=workout, **set_data)
        return workout

class UserWorkoutSerializer(serializers.ModelSerializer):
    sets = SetSerializer(source='workout_id.sets_set', many=True)

    class Meta:
        model = User_Workouts
        fields = ['id', 'username', 'workout_id', 'done_date', 'sets']
        read_only_fields = ['id', 'username']

class UserSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Sets
        fields = ['id', 'user_workout_id', 'set_id', 'reps', 'weight', 'username']
        read_only_fields = ['id', 'username']