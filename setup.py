from distutils.core import setup
import categories

try:
    long_description = open('README.txt').read()
except IOError:
    long_description = ''

setup(name='django-categories',
      version=catgories.get_version(),
      description='A way to handle one or more hierarchical category trees in django.',
      long_description=long_description,
      author='Corey Oordt',
      author_email='coordt@washingtontimes.com',
      url='http://opensource.washingtontimes.com/projects/django-categories/',
      packages=['categories', 'editor'],
      classifiers=['Development Status :: 4 - Beta',
          'Framework :: Django',
          'License :: OSI Approved :: Apache License',
          ],
      )
