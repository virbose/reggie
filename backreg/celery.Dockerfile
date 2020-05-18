FROM python:3.8-alpine

# Prepare for installing psycopg2
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# Set some env vars
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_SETTINGS_MODULE backreg.settings.default


# Set working dir
COPY . /app/django
WORKDIR /app/django

# Install requirements
COPY ./requirements.txt /app/django
RUN python -m pip install -r requirements.txt

