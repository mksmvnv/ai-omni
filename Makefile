.PHONY: all lint run

WORKDIR=./core

all: lint run

lint:
	@echo "Formatting..."
	@black $(WORKDIR) --config pyproject.toml
	@echo "Successfully!"

run:
	@echo "Running..."
	@python3 $(WORKDIR)/app.py