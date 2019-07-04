clean:
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.pytest_cache' -exec rm -fr {} +
	find . -name '.mypy_cache' -exec rm -fr {} +
	find . -name 'pip-wheel-metadata' -exec rm -fr {} +
	find . -name 'groupark.egg-info' -exec rm -fr {} +

test:
	pytest

COVFILE ?= .coverage

coverage: 
	mypy groupark
	export COVERAGE_FILE=$(COVFILE); pytest -x --cov=groupark tests/ \
	--cov-report term-missing -s -o cache_dir=/tmp/.pytest_cache

PART ?= patch

version:
	bump2version $(PART) pyproject.toml groupark/__init__.py --tag --commit
