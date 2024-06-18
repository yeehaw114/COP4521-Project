#!/bin/bash

echo "Creating migrations..."
python3 manage.py makemigrations
echo ======================


# Check if the custom permissions migration exists
if [ ! -f backend/auth/migrations/000X_assign_permissions.py ]; then
  echo "Creating custom permissions migration..."
  python3 manage.py makemigrations auth --empty --name assign_permissions
  echo "Editing the custom permissions migration..."
  cat <<EOF > backend/auth/migrations/000X_assign_permissions.py
from django.db import migrations

def assign_permissions(apps, schema_editor):
    Role = apps.get_model('auth', 'Role')
    Permission = apps.get_model('auth', 'Permission')
    
    admin_role = Role.objects.get(name='Admin')
    trainer_role = Role.objects.get(name='Trainer')
    user_role = Role.objects.get(name='User')

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
    dependencies = [
        ('auth', '000X_previous_migration'),  # Replace with the last migration file in the auth app
    ]

    operations = [
        migrations.RunPython(assign_permissions),
    ]
EOF
fi



echo "Starting migrations..."
python3 manage.py migrate
echo ======================

echo "Starting Server..."
python3 manage.py runserver 0.0.0.0:8080
echo ===================================