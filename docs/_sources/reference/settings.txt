.. _reference_settings:

========
Settings
========

The ``CATEGORIES_SETTINGS`` dictionary is where you can override the default settings. You don't have to include all the settings; only the ones which you want to override.

.. contents::
   :local:


The default settings are:

.. code-block:: python
	
	CATEGORIES_SETTINGS = {
	    'ALLOW_SLUG_CHANGE': False,
	    'CACHE_VIEW_LENGTH': 0,
	    'RELATION_MODELS': [],
	    'M2M_REGISTRY': {},
	    'FK_REGISTRY': {},
	    'THUMBNAIL_UPLOAD_PATH': 'uploads/categories/thumbnails',
	    'THUMBNAIL_STORAGE': settings.DEFAULT_FILE_STORAGE,
	    'SLUG_TRANSLITERATOR': lambda x: x,
	}


.. _ALLOW_SLUG_CHANGE:

ALLOW_SLUG_CHANGE
=================

**Default:** ``False``

**Description:** Changing the slug for a category can have serious consequences if it is used as part of a URL. Setting this to ``True`` will allow users to change the slug of a category.

.. _SLUG_TRANSLITERATOR:

SLUG_TRANSLITERATOR
===================

**Default:** ``lambda x: x``

**Description:** Allows the specification of a function to convert non-ASCII characters in the potential slug to ASCII characters. Allows specifying a ``callable()`` or a string in the form of ``'path.to.module.function'``.

A great tool for this is `Unidecode <http://pypi.python.org/pypi/Unidecode>`_. Use it by setting ``SLUG_TRANSLITERATOR`` to ``'unidecode.unidecode``.


.. _CACHE_VIEW_LENGTH:

CACHE_VIEW_LENGTH
=================

**Default:** ``0``

**Description:** This setting will be deprecated soon, but in the mean time, it allows you to specify the amount of time each view result is cached.

.. _RELATION_MODELS:

RELATION_MODELS
===============

**Default:** ``[]``

**Description:** Relation models is a set of models that a user can associate with this category. You specify models using ``'app_name.modelname'`` syntax.

.. _M2M_REGISTRY:

M2M_REGISTRY
============

**Default:** {}

**Description:** A dictionary where the keys are in ``'app_name.model_name'`` syntax, and the values are a string, dict, or tuple of dicts. See :ref:`registering_models`\ .

.. _FK_REGISTRY:

FK_REGISTRY
============

**Default:** {}

**Description:** A dictionary where the keys are in ``'app_name.model_name'`` syntax, and the values are a string, dict, or tuple of dicts. See :ref:`registering_models`\ .

.. _THUMBNAIL_UPLOAD_PATH:

THUMBNAIL_UPLOAD_PATH
=====================

**Default:** ``'uploads/categories/thumbnails'``

**Description:** Where thumbnails for the categories will be saved.

.. _THUMBNAIL_STORAGE:

THUMBNAIL_STORAGE
=================

**Default:** ``settings.DEFAULT_FILE_STORAGE``

**Description:** How to store the thumbnails. Allows for external storage engines like S3.

.. _JAVASCRIPT_URL:

JAVASCRIPT_URL
==============

**Default:** ``STATIC_URL or MEDIA_URL + 'js/'``

**Description:** Allows for customization of javascript placement.