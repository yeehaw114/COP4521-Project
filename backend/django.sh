#!/bin/bash

echo "Creating migrations..."
python3 manage.py makemigrations
echo ======================

echo "Starting migrations..."
python3 manage.py migrate
echo ======================

echo "Starting Server..."
python3 manage.py runserver 0.0.0.0:8080
echo ===================================
