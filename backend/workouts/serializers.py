from rest_framework import serializers
from .models import Workouts, Sets, User_Workouts, User_Sets

class UserSetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Sets
        fields = ['id', 'reps', 'weight']

class UserWorkoutsSerializer(serializers.ModelSerializer):
    sets = UserSetsSerializer(many=True, required=False)

    class Meta:
        model = User_Workouts
        fields = ['id', 'workout_id', 'username', 'done_date', 'sets']

        def create(self, validated_data):
            sets_data = validated_data.pop('sets', [])
            request_user = self.context['request'].user
            instance = User_Workouts.objects.create(username=request_user, **validated_data)

            if 'sets' in validated_data:
                for set_data in sets_data:
                    User_Sets.objects.create(user_workout_id=instance, **set_data)
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
        fields = ['id', 'name', 'username', 'sets']

        def create(self, validated_data):
            set_data = validated_data.pop('sets')
            request_user = self.context['request'].user
            instance = Workouts.objects.create(username=request_user, **validated_data)

            for set_data in set_data:
                Sets.objects.create(workout_id=instance, **set_data)
            return instance
