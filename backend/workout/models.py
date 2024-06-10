from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

class Sets(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    workout_id = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.CharField()
    reps = models.SmallIntegerField()
    weight = models.SmallIntegerField()

class User_Workouts(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    workout_id = models.ForeignKey(Workout, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    done_date = models.TimeField(auto_now_add=True)

class User_Sets(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    user_workout_id = models.ForeignKey(User_Workouts, on_delete=models.CASCADE)
    set_id = models.ForeignKey(Sets, on_delete=models.CASCADE)
    reps = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)