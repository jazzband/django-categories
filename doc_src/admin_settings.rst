.. _admin_settings:

==============================
Adding the fields to the Admin
==============================

By default, Django Categories adds the fields you configure to the model's Admin class. If your ModelAdmin class does not use the ``fieldsets`` attribute, the configured category fields are simply appended to the bottom the fields. If your ModelAdmin uses the ``fieldsets`` attribute, a new fieldset named ``Categories``, containing all the configured fields is appended to the fieldsets. You can override or alter this behavior with the :ref:`ADMIN_FIELDSETS` setting.

ADMIN_FIELDSETS allows you to:

* Prevent Django Categories from adding the fields or fieldsets to a model's ModelAdmin class.
* Change the name of the fieldset (from the default: "Categories")
* Change the placement of the fieldset (from the default: bottom)

Preventing fields in the admin class
====================================

If you don't want Django Categories to add any fields to the admin class, simply use the following format::

    CATEGORIES_SETTINGS = {
        'ADMIN_FIELDSETS': [
            'app.model': None,
        ]
    }

Changing the name of the field set
==================================

To rename the field set, use the following format::

    CATEGORIES_SETTINGS = {
        'ADMIN_FIELDSETS': [
            'app.model': 'Taxonomy',
        ]
    }

Putting the field set exactly where you want it
===============================================

For complete control over the field set, use the following format::

    CATEGORIES_SETTINGS = {
        'ADMIN_FIELDSETS': [
            'app.model': {
                'name': 'Categories',
                'index': 0
            },
        ]
    }
