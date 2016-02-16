help:
	@echo ""
	@echo "Available make commands:"
	@echo ""
	@echo "deps       Install development dependencies"
	@echo "test       Run tests"
	@echo "publish    Publish a release to PyPi (requires permissions)"
	@echo ""

deps:
	pip install -r requirements.txt
	pip install tox sphinx sphinx-autobuild

test:
	tox

publish:
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel --universal upload
	rm -fr build dist .egg requests.egg-info
