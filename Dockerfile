FROM python:3.9-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# psycopg2 dependencies
RUN apt-get update \
    && apt-get -y install libpq-dev gcc

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt --no-cache-dir --upgrade -r requirements.txt

COPY ./src /app/src
COPY ./migrations /app/migrations
