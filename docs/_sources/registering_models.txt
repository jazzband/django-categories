.. _registering_models:

==================
Registering Models
==================


Registering models in settings.py
=================================

It is nice to not have to modify the code of applications to add a relation to categories. You can therefore do all the registering in ``settings.py``\ . For example:

.. code-block:: python
	
	CATEGORIES_SETTINGS = {
	    'FK_REGISTRY': {
	        'app.AModel': 'category',
	        'app.MyModel': (
	            'primary_category', 
	            {'name': 'secondary_category', 'related_name': 'mymodel_sec_cat'}, )
	    },
	    'M2M_REGISTRY': {
	        'app.BModel': 'categories',
	        'app.MyModel': ('other_categories', 'more_categories', ),
	    }
	}

The ``FK_REGISTRY`` is a dictionary whose keys are the model to which to add the new field(s). The value is a string or tuple of strings or dictionaries specifying the necessary information for each field. 

The ``M2M_REGISTRY`` is a dictionary whose keys are the model to which to add the new field(s). The value is a string or tuple of strings specifying the necessary information for each field.


Registering one Category field to model
***************************************

The simplest way is to specify the name of the field, such as:

.. code-block:: python
	
	CATEGORIES_SETTINGS = {
	    'FK_REGISTRY': {
	        'app.AModel': 'category'
	    }
	}

This is equivalent to adding the following the ``AModel`` of ``app``\ :

.. code-block:: python
	
	category = models.ForeignKey(Category)


If you want more control over the new field, you can use a dictionary and pass other ``ForeignKey`` options. The ``name`` key is required:

.. code-block:: python
	
	CATEGORIES_SETTINGS = {
	    'FK_REGISTRY': {
	        'app.AModel': {'name': 'category', 'related_name': 'amodel_cats'}
	    }
	}

This is equivalent to adding the following the ``AModel`` of ``app``\ :

.. code-block:: python

	category = models.ForeignKey(Category, related_name='amodel_cats')

Registering two or more Category fields to a Model
**************************************************

When you want more than one relation to ``Category``\ , all but one of the fields must specify a ``related_name`` to avoid conflicts, like so:

.. code-block:: python
	
	CATEGORIES_SETTINGS = {
	    'FK_REGISTRY': {
	        'app.MyModel': (
	            'primary_category', 
	            {'name': 'secondary_category', 'related_name': 'mymodel_sec_cat'}, )
	    },

Registering one or more Many-to-Many Category fields to a Model
***************************************************************

.. code-block:: python
	
	CATEGORIES_SETTINGS = {
	    'M2M_REGISTRY': {
	        'app.AModel': 'categories',
	        'app.MyModel': (
	            {'name': 'other_categories', 'related_name': 'other_cats'}, 
	            {'name': 'more_categories', 'related_name': 'more_cats'}, 
	        ),
	    }
	}

.. _registering_a_m2one_relationship:

Registering a many-to-one relationship
======================================

To create a many-to-one relationship (foreign key) between a model and Django Categories, you register your model with the ``register_fk`` function.

.. py:function:: register_fk(model, field_name='category', extra_params={}])
   
   :param model: The Django Model to link to Django Categories
   :param field_name: Optional name for the field **default:** category
   :param extra_params: Optional dictionary of extra parameters passed to the ``ForeignKey`` class.

Example, in your ``models.py``::

	import categories
	categories.register_fk(MyModel)

If you want more than one field on a model you have to have some extra arguments::

	import categories
	categories.register_fk(MyModel, 'primary_category')
	categories.register_fk(MyModel, 'secondary_category', {'related_name':'mymodel_sec_cat'})

The ``extra_args`` allows you to specify the related_name of one of the fields so it doesn't clash.


Registering a many-to-many relationship
=======================================

To create a many-to-many relationship between a model and Django Categories, you register your model with the ``register_m2m`` function.

.. py:function:: register_m2m(model, field_name='categories', extra_params={}])
   
   :param model: The Django Model to link to Django Categories
   :param field_name: Optional name for the field **default:** categories
   :param extra_params: Optional dictionary of extra parameters passed to the ``ManyToManyField`` class.

Example, in your ``models.py``::

	import categories
	categories.register_m2m(MyModel)
