init:
	pyenv local 3.7.4

deps:
	pip install -r requirements.txt

test:
	pytest

.PHONY: init deps test