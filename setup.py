from distutils.core import setup

setup(name='django-categories',
      version='0.2',
      description='A way to handle one or more hierarchical category trees in django.',
      long_description='This app attempts to provide a generic category system that multiple apps could use. It uses MPTT for the tree storage and provides a custom admin for better visualization (copied and modified from feinCMS).',
      author='Corey Oordt',
      author_email='coordt@washingtontimes.com',
      url='http://opensource.washingtontimes.com/projects/django-categories/',
      packages=['categories', 'editor'],
      classifiers=['Development Status :: 4 - Beta',
          'Framework :: Django',
          'License :: OSI Approved :: Apache License',
          ],
      )

