FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y make

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD ["make", "run"]