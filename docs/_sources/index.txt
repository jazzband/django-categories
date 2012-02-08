=============================
Django Categories v |version|
=============================

Django Categories grew out of our need to provide a basic hierarchical taxonomy management system that multiple applications could use independently or in concert.

As a news site, our stories, photos, and other content get divided into "sections" and we wanted all the apps to use the same set of sections. As our needs grew, the Django Categories grew in the functionality it gave to category handling within web pages.

New in 1.0
==========

**Abstract Base Class for generic hierarchical category models**
   When you want a multiple types of categories and don't want them all part of the same model, you can now easily create new models by subclassing ``CategoryBase``. You can also add additional metadata as necessary.
   
   Your model's can subclass ``CategoryBaseAdminForm`` and ``CategoryBaseAdmin`` to get the hierarchical management in the admin.
   
   See the docs for more information.

**Increased the default caching time on views**
   The default setting for ``CACHE_VIEW_LENGTH`` was ``0``, which means it would tell the browser to *never* cache the page. It is now ``600``, which is the default for `CACHE_MIDDLEWARE_SECONDS <https://docs.djangoproject.com/en/1.3/ref/settings/#cache-middleware-seconds>`_

**Updated for use with Django-MPTT 0.5**
   Just a few tweaks.

**Initial compatibility with Django 1.4**
   More is coming, but at least it works.

**Slug transliteration for non-ASCII characters**
   A new setting, ``SLUG_TRANSLITERATOR``, allows you to specify a function for converting the non-ASCII characters to ASCII characters before the slugification. Works great with `Unidecode <http://pypi.python.org/pypi/Unidecode>`_.


Contents
========

.. toctree::
   :maxdepth: 2
   :glob:

   installation
   getting_started
   usage
   registering_models
   adding_the_fields
   custom_categories
   reference/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

