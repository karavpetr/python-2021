TESTS = tests

VENV ?= .venv
CODE = tests todo_list

.PHONY: venv
venv:
	python3 -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip
	$(VENV)/bin/python -m pip install flask
	$(VENV)/bin/python -m pip install pytest

.PHONY: test
test:
	$(VENV)/bin/pytest -v tests

.PHONY: up
up:
	FLASK_APP=todo_list.app $(VENV)/bin/flask run

