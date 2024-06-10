from rest_framework import serializers
from .models import Workouts, Sets, User_Workouts, User_Sets

class SetsSerializer(serializers.ModelSerializer):
    model = Sets
    fields = ['id', 'workout_id', 'exercise', 'reps', 'weight']

class WorkoutsSerializer(serializers.ModelSerializer):
    sets = SetsSerializer(many=True, read_only=True)

    class Meta:
        model = Workouts
        fields = ['id', 'name', 'username', 'sets']
    
    def create(self, validated_data):
        sets_data = validated_data.pop('sets')
        workout = Workouts.objects.create(**validated_data)
        for set_data in sets_data:
            Sets.objects.create(workout_id=workout, **set_data)
        return workout
    
    def update(self, instance, validated_data):
        sets_data = validated_data.pop('sets', [])
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        for set_data in sets_data:
            set_id = set_data.get('id', None)
            if set_id:
                set = Sets.objects.get(id=set_id)
                set.exercise = set_data.get('exercise', set.exercise)
                set.reps = set_data.get('reps', set.reps)
                set.weight = set_data.get('weight', set.weight)
                set.save()
            else:
                Sets.objects.create(workout_id=instance, **set_data)
        return instance

class UserWorkoutsSerializer(serializers.ModelSerializer):
    model = User_Workouts
    fields = ['id', 'workout_id', 'username', 'done_date']

class UserSetsSerializer(serializers.ModelSerializer):
    model = User_Sets
    fields = ['id', 'user_workout_id', 'set_id', 'reps', 'weight', 'username']