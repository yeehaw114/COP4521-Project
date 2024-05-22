FROM python:3.10

WORKDIR /app

COPY /backend/requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENTRYPOINT [ "python main.py" ]