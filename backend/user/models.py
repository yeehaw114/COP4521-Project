from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission
from django.db import models
from django.conf import settings

class Role(models.Model):
    Role = [
        ('Admin', 'Admin'),
        ('Trainer', 'Trainer'),
        ('User', 'User'),
    ]

    admin_group, created = Group.objects.get_or_create(name='Admin')
    user_group, created = Group.objects.get_or_create(name='User')

    # Define permissions
    add_user_permission = Permission.objects.get(codename='add_user')
    change_user_permission = Permission.objects.get(codename='change_user')
    delete_user_permission = Permission.objects.get(codename='delete_user')

    # Assign permissions to roles
    admin_group.permissions.add(add_user_permission, change_user_permission, delete_user_permission)
    user_group.permissions.add(change_user_permission)

    name = models.CharField(max_length=50, choices=Role, unique=True, verbose_name='Role')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='roles', verbose_name='Users with this Role')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, max_length=255, unique=True)
    role = models.ManyToManyField(Role)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return f'User(email={self.email}, username={self.username})'