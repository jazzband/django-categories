==================
Registering Models
==================


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
