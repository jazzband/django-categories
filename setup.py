from distutils.core import setup
import categories
import os

try:
    long_description = open('README.txt').read()
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
    author_email='coordt@washingtontimes.com',
    url='http://opensource.washingtontimes.com/projects/django-categories/',
    packages=['categories', 'editor'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'License :: OSI Approved :: Apache License',
    ],
    install_requires = reqs,
    dependency_links = [
        'http://opensource.washingtontimes.com/static/dist/django-mptt-0.3_pre.tar.gz#md5=2e7bf48ae24958ec3702314506f4fe99',
    ]
)
