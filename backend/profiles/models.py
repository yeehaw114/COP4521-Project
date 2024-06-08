from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username