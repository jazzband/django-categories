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
	pip install tox sphinx sphinx-autobuild twine

test:
	tox

publish:
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist
