FROM python:3.10.12

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./django.sh ./django.sh
COPY . ./

RUN chmod -R 777 ./django.sh


EXPOSE 8080

CMD [ "./django.sh" ]