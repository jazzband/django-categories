============
Installation
============

To use the Category model
=========================

1. Install django-categories::

    pip install django-categories

2. Add ``"categories"`` and ``"categories.editor"`` to your ``INSTALLED_APPS`` list in your project's ``settings.py`` file.

   .. code-block:: python

       INSTALLED_APPS = [
           # ...
           "categories",
           "categories.editor",
       ]

3. Run ``./manage.py syncdb`` (or ``./manage.py migrate categories`` if you are using `South <http://south.aeracode.org/>`_)


To only subclass CategoryBase
=============================

If you are going to create your own models using :py:class:`CategoryBase`, (see :ref:`creating_custom_categories`) you'll need a few different steps.

1. Install django-categories::

    pip install django-categories

2. Add ``"categories.editor"`` to your ``INSTALLED_APPS`` list in your project's ``settings.py`` file.

   .. code-block:: python

       INSTALLED_APPS = [
           # ...
           "categories.editor",
       ]

3. Create your own models.
