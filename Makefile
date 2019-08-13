init:
	pyenv local 3.7.4

run:
	python -m fpeel.fpeel --

deps:
	pip install -r requirements.txt

test:
	python -m pytest

.PHONY: init run deps test