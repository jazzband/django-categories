===============
Getting Started
===============

You can use Django Categories in two ways:

1. As storage for one tree of categories, using the :py:class:`Category` model::

	Top Category 1
	  Subcategory 1-1
	    Subcategory 1-2
	      subcategory 1-2-1
	Top Category 2
	  Subcategory 2-1

2. As the basis for several custom categories (see :ref:`creating_custom_categories`), e.g. a **MusicGenre** model
   
   ::
   
   	MusicGenre 1
   	  MusicSubGenre 1-1
   	  MusicSubGenre 1-2
   	    MusicSubGenre 1-2-1
   	MusicGenre 2
   	  MusicSubGenre 2-1
   
   and a **Subject** model
   
   ::
   
   	Subject 1
   	  Discipline 1-1
   	  Discipline 1-2
   	    SubDiscipline 1-2-1
   	Subject 2
   	  Discipline 2-1



Connecting your model with Django-Categories
============================================

There are two ways to add Category fields to an application. If you are in control of the code (it's your application) or you are willing to take control of the code (fork someone else's app) you can make a :ref:`hard_coded_connection`\ .

For 3rd-party apps or even your own apps that you don't wish to add Django-Categories as a dependency, you can configure a :ref:`lazy_connection`\ .

.. _hard_coded_connection:

Hard Coded Connection
---------------------

Hard coded connections are done in the exact same way you handle any other foreign key or many-to-many relations to a model.

.. code-block:: python

	from django.db import models

	class MyModel(models.Model):
	    name = models.CharField(max_length=100)
	    category = models.ForeignKey('categories.Category')

Don't forget to add the field or fields to your ``ModelAdmin`` class as well.


.. _lazy_connection:

Lazy Connection
---------------

Lazy connections are done through configuring Django Categories in the project's ``settings.py`` file. When the project starts up, the configured fields are dynamically added to the configured models and admin. 

If you do this before you have created the database (before you ran ``manage.py syncdb``), the fields will also be in the tables. If you do this after you have already created all the tables, you can run ``manage.py add_category_fields`` to create the fields (this requires Django South to be installed).

You add a many-to-one or many-to-many relationship with Django Categories using the :ref:`FK_REGISTRY` and :ref:`M2M_REGISTRY` settings respectively. For more information see :ref:`registering_models`\ .
