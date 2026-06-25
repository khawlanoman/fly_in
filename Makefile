PYTHON = python3 
PIP = $(PYTHON) -m pip
MAIN = fly-in.py

all: run

install:
	$(PIP) install flake8
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) $(MAIN)

debug:
	$(PYTHON) -m pdb $(MAIN)

clean:
	rm -rf __pycache__
	rm -rf src/models/__pycache__
	rm -rf src/parser/__pycache__
	rm -rf src/.mypy_cache
	rm -rf src/.pytest_cache
	rm -rf src/*.pyc

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict

