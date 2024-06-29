WORKDIR=./core

.PHONY: all lint build run

all: install lint build run

install:
		sudo apt install docker-compose && \
		sudo usermod -aG docker $$USER && \
		sudo service docker restart

lint:
		black $(WORKDIR) --config pyproject.toml

build:
		docker-compose up --build

run:
		python3 $(WORKDIR)/app.py

rm:
		docker-compose stop && \
		docker-compose rm && \
		rm -rf pgdata/