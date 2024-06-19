#!/bin/bash

function wait_for_postgres() {
    echo "Waiting for PostgreSQL to be ready..."
    while ! pg_isready -h db -p 5432 -U postgres; do
        sleep 1
    done
    echo "PostgreSQL is ready."
}

echo "Creating migrations..."
if python3 manage.py makemigrations; then
    echo "Migrations created successfully."
else
    echo "Error creating migrations."
    exit 1
fi
echo ======================

echo "Starting migrations..."
if python3 manage.py migrate; then
    echo "Migrations applied successfully."
else
    echo "Error applying migrations."
    exit 1
fi
echo ======================

echo "Starting Server..."
if python3 manage.py runserver 0.0.0.0:8080; then
    echo "Server started successfully."
else
    echo "Error starting server."
    exit 1
fi
echo ===================================

echo "Starting migrations..."
if python3 manage.py migrate; then
    echo "Migrations applied successfully."
else
    echo "Error applying migrations."
    exit 1
fi
echo ======================