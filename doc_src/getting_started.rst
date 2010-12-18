===============
Getting Started
===============

You can use Django Categories in two ways:

1. As storage for one tree of categories, e.g.::

	Top Category 1
	  Subcategory 1-1
	    Subcategory 1-2
	      subcategory 1-2-1
	Top Category 2
	  Subcategory 2-1

2. As a storage of several trees of categories, e.g.::

	Model 1
	  Category 1
	    Subcategory 1-1
	      Subcategory 1-2
	        subcategory 1-2-1
	  Category 2
	    Subcategory 2-1
	Model 2
	  Category 3
	    Subcategory 3-1
	      Subcategory 3-2
	        subcategory 3-2-1
	  Category 4
	    Subcategory 4-1

You can't do it as both at the same time, though.

Connecting your model with Django-Categories
============================================

Because there are a few additional methods and attributes that your model needs, you can't simply create a ``ForeignKey`` to ``Category``, even though that is eventually what happens.

You add a many-to-one or many-to-many relationship with Django Categories using the :py:func:`register_fk` and :py:func:`register_m2m` methods respectively. For example, if you added in your ``models.py``::

	import categories
	categories.register_fk(MyModel)

``MyModel`` would have a ``ForeignKey`` named ``category``
