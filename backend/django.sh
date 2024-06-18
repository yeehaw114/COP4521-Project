#!/bin/bash

echo "Creating migrations..."
python3 manage.py makemigrations
echo ======================

echo "Starting migrations..."
python3 manage.py migrate
echo ======================

echo "Starting role migrations..."
python3 manage.py migrate workouts 0001_initial.py --fake
echo ======================

echo "Starting Server..."
python3 manage.py runserver 0.0.0.0:8080
echo ===================================