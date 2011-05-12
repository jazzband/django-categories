from setuptools import setup, find_packages
import categories
import os

try:
    long_description = open('README.rst').read()
except IOError:
    long_description = ''

try:
    reqs = open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).read()
except (IOError, OSError):
    reqs = ''

setup(
    name='django-categories',
    version=categories.get_version(),
    description='A way to handle one or more hierarchical category trees in django.',
    long_description=long_description,
    author='Corey Oordt',
    author_email='coreyoordt@gmail.com',
    include_package_data=True,
    url='http://github.com/callowayproject/django-categories',
    packages=find_packages(),
    classifiers=[
        'Framework :: Django',
    ],
    install_requires = reqs,
    dependency_links = []
)
