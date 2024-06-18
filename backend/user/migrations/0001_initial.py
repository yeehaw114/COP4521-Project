from django.db import migrations

def create_initial_roles(apps, schema_editor):
    Role = apps.get_model('user', 'Role')
    roles = ['Admin', 'Trainer', 'User']
    for role in roles:
        Role.objects.create(name=role)

class Migration(migrations.Migration):
    operations = [
        migrations.RunPython(create_initial_roles)
    ]