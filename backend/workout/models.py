from django.db import models

# Tables
class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=60)
    description = models.CharField(max_length=500)
    join_date = models.TimeField()

class Exercise(models.Model):
    name = models.CharField(max_length=30)
    muscle_group = models.CharField(max_length=30)

class Workout_Exercises(models.Model):
    workout_id = models.CharField(max_length=10)
    exercise_name = models.CharField(max_length=30)
    reps = models.SmallIntegerField()
    weight = models.SmallIntegerField()

class Workout(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=30)

class User_Workouts(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    workout_id = models.CharField(max_length=10)
    username = models.CharField(max_length=30)
    done_date = models.TimeField()

class User_Sets(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    user_workout_id = models.CharField(max_length=10)
    reps = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    username = models.CharField(max_length=30)