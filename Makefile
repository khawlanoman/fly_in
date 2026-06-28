PYTHON = python3 
PIP = $(PYTHON) -m pip
MAIN = main.py

all: run

install:
	$(PIP) install flake8
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) $(MAIN) maps/easy/02_simple_fork.txt
debug:
	$(PYTHON) -m pdb $(MAIN)

clean:
	rm -rf __pycache__
	rm -rf src/models/__pycache__
	rm -rf src/__pycache__
	rm -rf src/parser/__pycache__
	rm -rf .mypy_cache

lint:
	-$(PYTHON) -m mypy main.py src/parser src/models \
		--warn-return-any \
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs
	$(PYTHON) -m flake8 .
