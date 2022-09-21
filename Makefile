.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

RELEASE_KIND := patch
SOURCE_DIR := categories

BRANCH_NAME := $(shell echo $$(git rev-parse --abbrev-ref HEAD))
SHORT_BRANCH_NAME := $(shell echo $(BRANCH_NAME) | cut -c 1-20)
PRIMARY_BRANCH_NAME := master
BUMPVERSION_OPTS :=

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

docs:  ## generate Sphinx HTML documentation, including API docs
	mkdir -p docs
	rm -f doc_src/api/$(SOURCE_DIR)*.rst
	ls -A1 docs | xargs -I {} rm -rf docs/{}
	$(MAKE) -C doc_src clean html
	cp -a doc_src/_build/html/. docs

pubdocs: docs  ## Publish the documentation to GitHub
	ghp-import -op docs

release-dev: RELEASE_KIND := dev
release-dev: do-release  ## Release a new development version: 1.1.1 -> 1.1.1+branchname-1

release-patch: RELEASE_KIND := patch
release-patch: do-release  ## Release a new patch version: 1.1.1 -> 1.1.2

release-minor: RELEASE_KIND := minor
release-minor: do-release  ## Release a new minor version: 1.1.1 -> 1.2.0

release-major: RELEASE_KIND := major
release-major: do-release  ## Release a new major version: 1.1.1 -> 2.0.0

release-version: get-version do-release  ## Release a specific version: release-version 1.2.3

#
# Helper targets. Not meant to use directly
#

do-release:
	@if [[ "$(BRANCH_NAME)" == "$(PRIMARY_BRANCH_NAME)" ]]; then \
		if [[ "$(RELEASE_KIND)" == "dev" ]]; then \
			echo "Error! Can't bump $(RELEASE_KIND) while on the $(PRIMARY_BRANCH_NAME) branch."; \
			exit; \
		fi; \
	elif [[ "$(RELEASE_KIND)" != "dev" ]]; then \
		echo "Error! Must be on the $(PRIMARY_BRANCH_NAME) branch to bump $(RELEASE_KIND)."; \
		exit; \
	fi; \
	git fetch -p --all; \
	generate-changelog; \
	export BRANCH_NAME=$(SHORT_BRANCH_NAME);bumpversion $(BUMPVERSION_OPTS) $(RELEASE_KIND) --allow-dirty; \
	git push origin $(BRANCH_NAME); \
	git push --tags;

get-version:  # Sets the value after release-version to the VERSION
	$(eval VERSION := $(filter-out release-version,$(MAKECMDGOALS)))
	$(eval BUMPVERSION_OPTS := --new-version=$(VERSION))

%: # NO-OP for unrecognized rules
	@:
