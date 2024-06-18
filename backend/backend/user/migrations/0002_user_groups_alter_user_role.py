# Generated by Django 5.0.6 on 2024-06-18 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0013_assign_permissions'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ManyToManyField(to='user.role'),
        ),
    ]
