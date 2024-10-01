.PHONY: all run lint

WORKDIR=./core
POETRYFLAGS=--config pyproject.toml

all: run lint

run:
	@echo "Running..."
	@poetry run python3 $(WORKDIR)/main.py

tests:
	@echo "Running tests..."
	@poetry run pytest $(WORKDIR)/tests

lint:
	@echo "Linting..."
	@black $(WORKDIR) $(POETRYFLAGS)
	@echo "Linting done!"