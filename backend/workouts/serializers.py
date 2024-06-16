from rest_framework import serializers
from .models import Workouts, Sets, User_Workouts, User_Sets

class LogSetSerializer(serializers.Serializer):
    exercise = serializers.CharField(max_length=50, required=True)
    reps = serializers.IntegerField(required=True)
    weight = serializers.IntegerField(required=True)

class UserSetsSerializer(serializers.ModelSerializer):
    exercise = serializers.CharField(source='set_id.exercise', read_only=True)
    class Meta:
        model = User_Sets
        fields = ['id', 'exercise', 'reps', 'weight']

class UserWorkoutsSerializer(serializers.ModelSerializer):
    sets = UserSetsSerializer(many=True, required=False)

    class Meta:
        model = User_Workouts
        fields = ['id', 'workout_id', 'done_date', 'sets', 'username']
        read_only_fields = ['username']

        def create(self, validated_data):
            sets_data = validated_data.pop('sets', [])
            request_user = self.context['request'].user
            instance = User_Workouts.objects.create(username=request_user, **validated_data)

            if 'sets' in validated_data:
                for set_data in sets_data:
                    exercise = set_data.pop('exercise')
                    set_instance = Sets.objects.get_or_create(workout_id=instance.workout_id, exercise=exercise, default={'reps': set_data.get('reps', 0), 'weight': set_data.get('weight', 0)})
                    User_Sets.objects.create(user_workout_id=instance, set_id=set_instance, **set_data)
            return instance

class SetsSerializer(serializers.ModelSerializer):
    exercise = serializers.CharField(max_length=50, required=True)

    class Meta:
        model = Sets
        fields = ['id', 'exercise', 'reps', 'weight']

class WorkoutsSerializer(serializers.ModelSerializer):
    sets = SetsSerializer(many=True, required=False)

    class Meta:
        model = Workouts
        fields = ['id', 'name', 'sets']

        def create(self, validated_data):
            set_data = validated_data.pop('sets')
            request_user = self.context['request'].user
            instance = Workouts.objects.create(username=request_user, **validated_data)

            for set_data in set_data:
                Sets.objects.create(workout_id=instance, **set_data)
            return instance