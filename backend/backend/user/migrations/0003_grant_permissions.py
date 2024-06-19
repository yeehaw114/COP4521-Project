from django.db import migrations, connection

def grant_permissions(apps, schema_editor):
    with connection.cursor() as cursor:
        # Creating roles if they don't exist
        cursor.execute("DO $$ BEGIN IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'admin') THEN CREATE ROLE admin; END IF; END $$;")
        cursor.execute("DO $$ BEGIN IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'premium') THEN CREATE ROLE premium; END IF; END $$;")
        cursor.execute("DO $$ BEGIN IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'free') THEN CREATE ROLE free; END IF; END $$;")

        # Creating users if they don't exist
        cursor.execute("DO $$ BEGIN IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'app_admin') THEN CREATE USER app_admin WITH PASSWORD 'admin_password'; END IF; END $$;")
        cursor.execute("DO $$ BEGIN IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'app_premium') THEN CREATE USER app_premium WITH PASSWORD 'premium_password'; END IF; END $$;")
        cursor.execute("DO $$ BEGIN IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'app_free') THEN CREATE USER app_free WITH PASSWORD 'free_password'; END IF; END $$;")
        
        # Granting roles to users
        cursor.execute("GRANT admin TO app_admin;")
        cursor.execute("GRANT premium TO app_premium;")
        cursor.execute("GRANT free TO app_free;")
        
        
        # Granting full permissions to Admin
        cursor.execute("""
            GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO admin;
            GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO admin;
        """)
        # Granting specific permissions to Premium
        cursor.execute("""
            GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE workouts_workouts TO premium;
            GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE workouts_sets TO premium;
            GRANT SELECT ON TABLE workouts_user_sets TO premium;
            GRANT SELECT ON TABLE workouts_user_workouts TO premium;
        """)
        # Granting specific permissions to Free
        cursor.execute("""
            GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE workouts_user_sets TO free;
            GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE workouts_user_workouts TO free;
            GRANT SELECT ON TABLE workouts_workouts TO free;
            GRANT SELECT ON TABLE workouts_sets TO free;
        """)


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
        ('user', '0002_role_permissions'),
        ('auth', '0013_assign_permissions'),
    ]

    operations = [
        migrations.RunPython(grant_permissions),
    ]
