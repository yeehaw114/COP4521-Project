# backend/user/migrations/0001_initial.py

from django.conf import settings
from django.db import migrations, models
from django.contrib.auth.models import Permission

def create_initial_roles(apps, schema_editor):
    Role = apps.get_model('backend.user', 'Role')
    Permission = apps.get_model('auth', 'Permission')

    admin_role = Role.objects.create(name='Admin')
    trainer_role = Role.objects.create(name='Trainer')
    user_role = Role.objects.create(name='User')

    all_permissions = Permission.objects.filter(codename__in=[
        'can_view_workouts', 'can_edit_workouts', 'can_delete_workouts',
        'can_view_sets', 'can_edit_sets', 'can_delete_sets',
        'can_view_userworkouts', 'can_edit_userworkouts', 'can_delete_userworkouts',
        'can_view_usersets', 'can_edit_usersets', 'can_delete_usersets',
    ])

    trainer_permissions = Permission.objects.filter(codename__in=[
        'can_view_workouts', 'can_edit_workouts', 'can_delete_workouts',
        'can_view_sets', 'can_edit_sets', 'can_delete_sets',
        'can_view_userworkouts', 'can_view_usersets'
    ])

    user_permissions = Permission.objects.filter(codename__in=[
        'can_view_workouts', 'can_view_sets',
        'can_view_userworkouts', 'can_edit_userworkouts', 'can_delete_userworkouts',
        'can_view_usersets', 'can_edit_usersets', 'can_delete_usersets',
    ])

    admin_role.permissions.set(all_permissions)
    trainer_role.permissions.set(trainer_permissions)
    user_role.permissions.set(user_permissions)

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, max_length=255, unique=True)),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True)),
                ('role', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Admin', 'Admin'), ('Trainer', 'Trainer'), ('User', 'User')], max_length=50, unique=True, verbose_name='Role')),
                ('users', models.ManyToManyField(related_name='roles', to=settings.AUTH_USER_MODEL, verbose_name='Users with this Role')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        
        migrations.RunPython(create_initial_roles),  # Added custom operation
    ]
