include .env.template
export $(shell sed 's/=.*//' .env)

.PHONY: help clean clean-build coverage migrations

.DEFAULT: help

help:
	@echo "make clean"
	@echo "       remove all build, test, coverage and Python artifacts"
	@echo "make clean-build"
	@echo "       remove build artifacts"
	@echo "make coverage"
	@echo "       check code coverage"
	@echo "make lint"
	@echo "       check style with flake8"
	@echo "make test"
	@echo "       run tests"

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . | grep -E "__pycache__|.pyc" | xargs rm -rf

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

coverage:
	python3 -m pip install pytest pytest-cov
	python3 -m pytest --cov-report xml --cov=./

test:
	python3 -m pytest -s tests/

coverage-report:
	pytest tests/ --cov-report term --cov=./

coverage-missing:
	pytest tests/ --cov-report term-missing --cov=./

lint:
	flake8

first-migration:
	alembic -c migrations/alembic/alembic.ini revision --autogenerate -m"First commit"

migrations:
	alembic -c migrations/alembic/alembic.ini upgrade head

run:
	python .