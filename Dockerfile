FROM python:3.12

WORKDIR /app

RUN pip install --no-cache-dir poetry

ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    PYTHONUNBUFFERED=1

COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-root --no-dev

COPY . /app