FROM python:latest

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

ENV IS_PRODUCTION 1
