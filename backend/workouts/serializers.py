from rest_framework import serializers
from .models import Workouts, Sets, User_Workouts, User_Sets

class UserSetsSerializer(serializers.ModelSerializer):
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
        fields = ['id', 'name', 'sets']

        def create(self, validated_data):
            set_data = validated_data.pop('sets')
            request_user = self.context['request'].user
            instance = Workouts.objects.create(username=request_user, **validated_data)

            for set_data in set_data:
                Sets.objects.create(workout_id=instance, **set_data)
            return instance
        
        def update(self, instance, validated_data):
            sets_data = validated_data.pop('sets', [])
            instance.name = validated_data.get('name', instance.name)
            instance.save()

            current_set_ids = [item['id'] for item in sets_data if 'id' in item]
            Sets.objects.filter(workout_id=instance).exclude(id__in=current_set_ids).delete()

            for set_data in sets_data:
                set_id = set_data.get('id', None)
                if set_id:
                    set_instance = Sets.objects.get(id=set_id, workout_id=instance)
                    set_instance.exercise = set_data.get('exercise', set_instance.exercise)
                    set_instance.reps = set_data.get('reps', set_instance.reps)
                    set_instance.weight = set_data.get('weight', set_instance.weight)
                    set_instance.save()
                else:
                    Sets.objects.create(workout_id=instance, **set_data)

            return instance