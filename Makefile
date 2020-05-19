.PHONY: docs test

all: wheel

ON_TAG := $(shell git tag --points-at HEAD)

test:
	pip install pytest
	PYTHONPATH=. pytest

wheel: test
	rm -rf wheelhouse
	mkdir wheelhouse
	pip wheel -v --wheel-dir=wheelhouse .

publish: wheel
	pip install twine
	twine upload wheelhouse/etcetera*.whl -u __token__ -p $(PYPI_TOKEN)

maybe_publish: wheel
ifneq ($(ON_TAG),)
	pip install twine
	twine upload wheelhouse/etcetera*.whl -u __token__ -p $(PYPI_TOKEN)
endif

docs:
	(cd docs; make html)

