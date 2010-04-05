==================
Registering Models
==================




You can register models with the 

import categories
categories.register_fk(MyModel)

or

import categories
categories.register_m2m(MyModel)

If you want more than one field on a model you have to have some extra arguments

	import categories
	categories.register_fk(MyModel, 'primary_category')
	categories.register_fk(MyModel, 'secondary_category', {'related_name':'mymodel_sec_set'})

The ``extra_args`` allows you to specify the related_name of one of the fields so it doesn't clash.


Extra fields with Many-to-Many Categories
=========================================

Occasionally you may want to add one or more fields to the categories you relate to a given model. For example, you may want an easy way to select one of the categories to be "primary." This requires a bit more work.

1. Create the intermediary class::

	from categories.models import CategoryIntermediary
	
	# We're assuming that there is a ``Blog`` model previously defined 
	# or imported
	class BlogCategories(CategoryIntermediary):
		blog = models.ForeignKey(Blog)
	
	categories.register_m2m(Blog, extra_args={'through':'BlogCategories'})