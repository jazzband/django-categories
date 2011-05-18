Django Categories grew out of our need to provide a basic hierarchical taxonomy management system that multiple applications could use independently or in concert.

As a news site, our stories, photos, and other content get divided into "sections" and we wanted all the apps to use the same set of sections. As our needs grew, the Django Categories grew in the functionality it gave to category handling within web pages.

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