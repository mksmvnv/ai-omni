FROM python:3.12

RUN apt update && apt upgrade

WORKDIR /app
COPY . /app

RUN pip install poetry
RUN poetry install
RUN poetry run alembic upgrade head




