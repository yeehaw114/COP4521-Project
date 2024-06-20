FROM python:3.10.12

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y bash

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code including django.sh and wait-for-it.py
COPY . .

# Ensure the django.sh script is executable
RUN chmod +x ./django.sh

EXPOSE 8080

CMD ["./django.sh"]
