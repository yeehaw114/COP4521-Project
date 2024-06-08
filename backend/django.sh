#!/bin/bash

echo "Making migrations..."
python3 manage.py migrate
echo ======================

echo "Starting Server..."
python3 manage.py runserver 0.0.0.0:8080
echo ===================================