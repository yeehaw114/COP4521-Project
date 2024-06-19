from django.db import migrations, models
from django.conf import settings
from django.contrib.auth.models import Permission

def create_initial_roles(apps, schema_editor):
    Role = apps.get_model('user', 'Role')
    Permission = apps.get_model('auth', 'Permission')

    admin_role = Role.objects.create(name='Admin')
    premium_role = Role.objects.create(name='Premium')
    free_role = Role.objects.create(name='Free')

    all_permissions = Permission.objects.filter(codename__in=[
        'can_view_workouts', 'can_edit_workouts', 'can_delete_workouts',
        'can_view_sets', 'can_edit_sets', 'can_delete_sets',
        'can_view_user_workouts', 'can_edit_user_workouts', 'can_delete_user_workouts',
        'can_view_user_sets', 'can_edit_user_sets', 'can_delete_user_sets',
    ])

    premium_permissions = Permission.objects.filter(codename__in=[
        'can_view_workouts', 'can_edit_workouts', 'can_delete_workouts',
        'can_view_sets', 'can_edit_sets', 'can_delete_sets',
        'can_view_user_workouts', 'can_view_user_sets'
    ])

    free_permissions = Permission.objects.filter(codename__in=[
        'can_view_workouts', 'can_view_sets',
        'can_view_user_workouts', 'can_edit_user_workouts', 'can_delete_user_workouts',
        'can_view_user_sets', 'can_edit_user_sets', 'can_delete_user_sets',
    ])

    admin_role.permissions.set(all_permissions)
    premium_role.permissions.set(premium_permissions)
    free_role.permissions.set(free_permissions)

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0013_assign_permissions'),
    ]

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
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Admin', 'Admin'), ('Premium', 'Premium'), ('Free', 'Free')], max_length=50, unique=True, verbose_name='Role')),
                ('users', models.ManyToManyField(related_name='role_users', to=settings.AUTH_USER_MODEL, verbose_name='Users with this Role')),
                ('permissions', models.ManyToManyField(related_name='role_permissions', to='auth.Permission', verbose_name='Permissions for this Role')),  # Ensure this line is included
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(to='user.Role', related_name='role_users'),
        ),
        migrations.RunPython(create_initial_roles),
    ]
