WORKDIR=./core

.PHONY: all lint run

all: lint run

lint:
		black $(WORKDIR) --config pyproject.toml

run:
		python3 $(WORKDIR)/app.py