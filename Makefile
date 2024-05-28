WORKDIR=./core

all: lint run

lint:
	black $(WORKDIR) --config pyproject.toml
run:
	python3 $(WORKDIR)/app.py