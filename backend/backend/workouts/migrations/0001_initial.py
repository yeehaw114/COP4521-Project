# Generated by Django 5.0.6 on 2024-06-19 15:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sets',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('exercise', models.CharField(max_length=100)),
                ('reps', models.SmallIntegerField()),
                ('weight', models.SmallIntegerField()),
            ],
            options={
                'permissions': [('can_view_sets', 'Can view Sets'), ('can_edit_sets', 'Can edit Sets'), ('can_delete_sets', 'Can delete Sets')],
            },
        ),
        migrations.CreateModel(
            name='User_Workouts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('done_date', models.TimeField(auto_now_add=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('can_view_user_workouts', 'Can view User Workouts'), ('can_edit_user_workouts', 'Can edit User Workouts'), ('can_delete_user_workouts', 'Can delete User Workouts')],
            },
        ),
        migrations.CreateModel(
            name='User_Sets',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reps', models.SmallIntegerField()),
                ('weight', models.SmallIntegerField()),
                ('set_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.sets')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_workout_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.user_workouts')),
            ],
            options={
                'permissions': [('can_view_user_sets', 'Can view User Sets'), ('can_edit_user_sets', 'Can edit User Sets'), ('can_delete_user_sets', 'Can delete User Sets')],
            },
        ),
        migrations.CreateModel(
            name='Workouts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('can_view_workouts', 'Can view Workouts'), ('can_edit_workouts', 'Can edit Workouts'), ('can_delete_workouts', 'Can delete Workouts')],
            },
        ),
        migrations.AddField(
            model_name='user_workouts',
            name='workout_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.workouts'),
        ),
        migrations.AddField(
            model_name='sets',
            name='workout_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.workouts'),
        ),
    ]
