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


