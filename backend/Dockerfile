FROM python:3.10.12

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y bash

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

EXPOSE 8080

ENTRYPOINT [ "./django.sh" ]