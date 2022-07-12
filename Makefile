.DEFAULT_GOAL := help

# Grab virtualenv name from the shell or init default
NAME = pylangoo
VENV = $(shell echo $${VIRTUAL_ENV-env})
PY3 := $(shell command -v python3 2> /dev/null)
PIP = $(VENV)/bin/pip
PYTHON = $(VENV)/bin/python3

.PHONY: all
all: check install lint test

.DEFAULT: help
help:
	@echo "Utilities to be able to develop and use PyLangoo locally."
	@echo
	@echo "   $$ make all  --> Run all steps but clean"
	@echo "   $$ make install --> Install depenencies"
	@echo "   $$ make lint --> Run linter"
	@echo "   $$ make test --> Run tests"
	@echo "   $$ make clean --> Clean up project"

.PHONY: check
check $(PYTHON):
	@if [ -z $(PY3) ]; then echo "Python 3 could not be found."; exit 2; fi
	$(PY3) -m venv $(VENV)

.PHONY: install
install:
	@echo "Installing full environment locally into the virtualenv"
	$(PIP) install -e .[all]
	$(PIP) install -r requirements.txt

.PHONY: lint
lint:
	$(PYTHON) -m black tests -t py310 ./pylangoo ./tests
	$(PYTHON) -m isort --settings-path=./.isort.cfg ./pylangoo ./tests
	$(PYTHON) -m flake8 ./pylangoo ./tests

.PHONY: test
test:
	$(PYTHON) -m pytest ./tests/ --cov-report term-missing --cov $(NAME) # --cov-fail-under 100 

.PHONY: clean
clean:
	find . -type d -name "__pycache__" | xargs rm -rf {};
	rm -rf $(VENV)