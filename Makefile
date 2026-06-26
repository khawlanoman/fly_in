PYTHON = python3 
PIP = $(PYTHON) -m pip
MAIN = main.py

all: run

install:
	$(PIP) install flake8
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) $(MAIN) maps/hard/03_ultimate_challenge.txt
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
# Run flake8
#$(PYTHON) -m flake8 .

# Run mypy
	$(PYTHON) -m mypy main.py src/parser src/models \
		--warn-return-any \
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs
