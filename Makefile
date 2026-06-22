
install:
	python3 -m pip install -r requirements.txt

run:
	python3 main.py  maps/hard/03_ultimate_challenge.txt

debug:
	python3 -m pdb main.py

clean:
	rm -rf __pycache__
	rm -rf src/models/__pycache__
	rm -rf src/parser/__pycache__

lint:
	flake8 .
	mypy . \
		--warn-return-any \
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs

.PHONY: install run debug clean lint