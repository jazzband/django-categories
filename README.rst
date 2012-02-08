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

Updated in 0.8.8
================

The `editor` app was placed inside the categories app, `categories.editor`, to avoid any name clashes.

Upgrading
---------

A setting change is all that is needed::

    INSTALLED_APPS = (
        'categories',
        'categories.editor',
    )

New in 0.8
==========

**Added an active field**
	As an alternative to deleting categories, you can make them inactive.
	
	Also added a manager method ``active()`` to query only the active categories and added Admin Actions to activate or deactivate an item.

**Improved import**
	Previously the import saved items in the reverse order to the imported file. Now them import in order.

New in 0.7
==========

**Added South migrations**
	All the previous SQL scripts have been converted to South migrations.

**Can add category fields via management command (and South)**
	The new ability to setup category relationships in ``settings.py`` works fine if you are starting from scratch, but not if you want to add it after you have set up the database. Now there is a management command to make sure all the correct fields and tables are created.

**Added an alternate_url field**
	This allows the specification of a URL that is not derived from the category hierarchy.

**New JAVASCRIPT_URL setting**
	This allows some customization of the ``genericcollections.js`` file.

**New get_latest_objects_by_category template tag**
	This will do pretty much what it says.


New in 0.6
==========

**Class-based views**
	Works great with Django 1.3 or `django-cbv <http://pypi.python.org/pypi/django-cbv>`_

**New Settings infrastructure**
	To be more like the Django project, we are migrating from individual CATEGORIES_* settings to a dictionary named ``CATEGORIES_SETTINGS``\ . Use of the previous settings will still work but will generate a ``DeprecationError``\ .

**The tree's initially expanded state is now configurable**
	``EDITOR_TREE_INITIAL_STATE`` allows a ``collapsed`` or ``expanded`` value. The default is ``collapsed``\ .

**Optional Thumbnail field**
	Have a thumbnail for each category!

**"Categorize" models in settings**
	Now you don't have to modify the model to add a ``Category`` relationship. Use the new settings to "wire" categories to different models.

Features of the project
=======================

**Multiple trees, or a single tree**
	You can treat all the records as a single tree, shared by all the applications. You can also treat each of the top level records as individual trees, for different apps or uses.

**Easy handling of hierarchical data**
	We use `Django MPTT <http://pypi.python.org/pypi/django-mptt>`_ to manage the data efficiently and provide the extra access functions.

**Easy importation of data**
	Import a tree or trees of space- or tab-indented data with a Django management command.

**Metadata for better SEO on web pages**
	Include all the metadata you want for easy inclusion on web pages.

**Link uncategorized objects to a category**
	Attach any number of objects to a category, even if the objects themselves aren't categorized.

**Hierarchical Admin**
	Shows the data in typical tree form with disclosure triangles

**Template Helpers**
	Easy ways for displaying the tree data in templates:

	**Show one level of a tree**
		All root categories or just children of a specified category
	
	**Show multiple levels**
		Ancestors of category, category and all children of category or  a category and its children

Contributors
============

* Corey Oordt      http://github.com/coordt
* Erik Simmler     http://github.com/tgecho
* Martin Ogden     http://github.com/martinogden
* Ramiro Morales   http://github.com/ramiro
* Evan Culver      http://github.com/eculver
* Andrzej Herok    http://github.com/aherok
* Jonathan Hensley 
* Justin Quick     http://github.com/justquick
* Josh Ourisman    http://github.com/joshourisman
* Jose Soares      http://github.com/josesoa