from django.db import models
from user.models import User
class Workouts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"Workout(user={self.username}, name={self.name})"


class Sets(models.Model):
    id = models.AutoField(primary_key=True)
    workout_id = models.ForeignKey(Workouts, on_delete=models.CASCADE)
    exercise = models.CharField()  
    reps = models.SmallIntegerField()
    weight = models.SmallIntegerField()

    def __str__(self):
        return f"Set(workout={self.workout_id}, exercise={self.exercise}, reps={self.reps}, weight={self.weight})"


class User_Workouts(models.Model):
    id = models.AutoField(primary_key=True)
    workout_id = models.ForeignKey(Workouts, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    done_date = models.TimeField(auto_now_add=True)


    def __str__(self):
        return f"User_Workout(user={self.username}, workout={self.workout_id}, date={self.done_date})"


class User_Sets(models.Model):
    id = models.AutoField(primary_key=True)
    user_workout_id = models.ForeignKey(User_Workouts, on_delete=models.CASCADE)
    exercise = models.CharField()
    reps = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"User_Set(user={self.username}, exercise={self.exercise}, reps={self.reps}, weight={self.weight})"