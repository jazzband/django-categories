============
Installation
============

1. Install django-categories::

    pip install django-categories

2. Add ``"categories"`` and ``"editor"`` to your ``INSTALLED_APPS`` list in your project's ``settings.py`` file.

   .. code-block:: python

       INSTALLED_APPS = [
           # ...
           "categories",
           "categories.editor",
       ]

3. Run ``./manage.py syncdb`` (or ``./manage.py migrate categories`` if you are using `South <http://south.aeracode.org/>`_)
