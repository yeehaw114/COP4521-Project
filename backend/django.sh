#!/bin/bash

echo "Waiting for 5 seconds..."
sleep 5
echo "Done waiting, proceeding with migrations and server startup..."

echo "Creating migrations..."
if python3 manage.py makemigrations; then
    echo "Migrations created successfully."
else
    echo "Error creating migrations."
    exit 1
fi
echo ======================
echo "Starting migrations..."

# Retry logic for applying migrations
RETRY_COUNT=0
MAX_RETRIES=5
SUCCESS=false

until [ $RETRY_COUNT -ge $MAX_RETRIES ]
do
    if python3 manage.py migrate; then
        echo "Migrations applied successfully."
        SUCCESS=true
        break
    else
        echo "Error applying migrations. Retrying in 5 seconds..."
        RETRY_COUNT=$((RETRY_COUNT+1))
        sleep 5
    fi
done

if [ "$SUCCESS" = false ]; then
    echo "Failed to apply migrations after $RETRY_COUNT retries."
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
