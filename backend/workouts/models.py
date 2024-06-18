from django.db import models
from user.models import User

class Workouts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_view_workouts", "Can view Workouts"),
            ("can_edit_workouts", "Can edit Workouts"),
            ("can_delete_workouts", "Can delete Workouts"),
        ]

    def __str__(self):
        return f"Workout(user={self.username}, name={self.name})"

class Sets(models.Model):
    id = models.AutoField(primary_key=True)
    workout_id = models.ForeignKey(Workouts, on_delete=models.CASCADE)
    exercise = models.CharField()
    reps = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    permissions = [
            ("can_view_sets", "Can view Sets"),
            ("can_edit_sets", "Can edit Sets"),
            ("can_delete_sets", "Can delete Sets"),
        ]

    def __str__(self):
        return f"Set(workout={self.workout_id}, exercise={self.exercise}, reps={self.reps}, weight={self.weight})"

class User_Workouts(models.Model):
    id = models.AutoField(primary_key=True)
    workout_id = models.ForeignKey(Workouts, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    done_date = models.TimeField(auto_now_add=True)
    permissions = [
            ("can_view_userworkouts", "Can view UserWorkouts"),
            ("can_edit_userworkouts", "Can edit UserWorkouts"),
            ("can_delete_userworkouts", "Can delete UserWorkouts"),
        ]

    def __str__(self):
        return f"User_Workout(user={self.username}, workout={self.workout_id}, date={self.done_date})"

class User_Sets(models.Model):
    id = models.AutoField(primary_key=True)
    user_workout_id = models.ForeignKey(User_Workouts, on_delete=models.CASCADE)
    set_id = models.ForeignKey(Sets, on_delete=models.CASCADE)
    reps = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    permissions = [
            ("can_view_usersets", "Can view UserSets"),
            ("can_edit_usersets", "Can edit UserSets"),
            ("can_delete_usersets", "Can delete UserSets"),
        ]

    def __str__(self):
        return f"User_Set(user={self.username}, set={self.set_id}, reps={self.reps}, weight={self.weight})"