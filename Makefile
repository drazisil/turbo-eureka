init:
	pyenv local 3.7.4

deps:
	pip install -r requirements.txt

test:
	python -m pytest

.PHONY: init deps test