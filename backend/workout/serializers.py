from rest_framework import serializers
from .models import Workout, Workout_Exercises, Exercise

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['name', 'muscle_group']

class WorkoutExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout_Exercises
        fields = ['exercise_name', 'reps', 'weight']

class WorkoutSerializer(serializers.ModelSerializer):
    exercises = WorkoutExercisesSerializer(many=True)

    class Meta:
        model = Workout
        fields = ['id', 'name', 'exercises']
        
    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises')
        workout = Workout.objects.create(**validated_data)
        for exercise_data in exercises_data:
            Workout_Exercises.objects.create(workout_id=workout.id, **exercise_data)
        return workout