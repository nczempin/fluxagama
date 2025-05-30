.PHONY: default deps lint test wheel run

DEFAULT_TARGETS := deps lint test wheel

# default target: install deps, run linter & tests, build wheel
default: $(DEFAULT_TARGETS)

# install python dependencies
deps:
	pip install -r requirements.txt

lint:
	flake8 src tests

test:
	pytest

wheel:
	python setup.py bdist_wheel

# optional run target to launch the game
run:
	python -m fluxagama.fluxagama
