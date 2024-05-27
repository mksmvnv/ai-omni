PROJECT_DIR=core

all: lint

lint:
	poetry run python -m black $(PROJECT_DIR) --config pyproject.toml