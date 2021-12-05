.DEFAULT_GOAL := help

RELEASE_KIND := patch
SOURCE_DIR := categories

BRANCH_NAME := $(shell echo $$(git rev-parse --abbrev-ref HEAD))
SHORT_BRANCH_NAME := $(shell echo $(BRANCH_NAME) | cut -c 1-20)
PRIMARY_BRANCH_NAME := master

EDIT_CHANGELOG_IF_EDITOR_SET := @bash -c "$(shell if [[ -n $$EDITOR ]] ; then echo "$$EDITOR CHANGELOG.md" ; else echo "" ; fi)"

help:
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | sort | awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

deps:  ## Install development dependencies
	pip install -r requirements.txt
	pip install tox sphinx sphinx-autobuild twine

test:  ## Run tests
	tox

publish:  ## Publish a release to PyPi (requires permissions)
	rm -fr build dist
	python setup.py sdist bdist_wheel
	twine upload dist/*

release-helper:
	## DO NOT CALL DIRECTLY. It is used by release-{patch,major,minor,dev}
	@echo "Branch In Use: $(BRANCH_NAME) $(SHORT_BRANCH_NAME)"
ifeq ($(BRANCH_NAME), $(PRIMARY_BRANCH_NAME))
	ifeq ($(RELEASE_KIND), dev)
		@echo "Error! Can't bump $(RELEASE_KIND) while on the $(PRIMARY_BRANCH_NAME) branch."
		exit
else ifneq ($(RELEASE_KIND), dev)
	@echo "Error! Must be on the $(PRIMARY_BRANCH_NAME) branch to bump $(RELEASE_KIND)."
	exit
endif

	git fetch -p --all
	gitchangelog
	$(EDIT_CHANGELOG_IF_EDITOR_SET)
	export BRANCH_NAME=$(SHORT_BRANCH_NAME);bumpversion $(RELEASE_KIND) --allow-dirty --tag
	git push origin $(BRANCH_NAME)
	git push --tags

set-release-major-env-var:
	$(eval RELEASE_KIND := major)

set-release-minor-env-var:
	$(eval RELEASE_KIND := minor)

set-release-patch-env-var:
	$(eval RELEASE_KIND := patch)

set-release-dev-env-var:
	$(eval RELEASE_KIND := dev)

release-dev: set-release-dev-env-var release-helper  ## Release a new development version: 1.1.1 -> 1.1.1+branchname-0

release-patch: set-release-patch-env-var release-helper  ## Release a new patch version: 1.1.1 -> 1.1.2

release-minor: set-release-minor-env-var release-helper  ## Release a new minor version: 1.1.1 -> 1.2.0

release-major: set-release-major-env-var release-helper  ## release a new major version: 1.1.1 -> 2.0.0
