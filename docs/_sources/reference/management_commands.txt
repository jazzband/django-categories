.. _management-commands:

===================
Management Commands
===================

.. _import_categories:

import_categories
=================

**Usage:** ``./manage.py import_categories /path/to/file.txt [/path/to/file2.txt]``

Imports category tree(s) from a file. Sub categories must be indented by the same multiple of spaces or tabs. The first line in the file cannot start with a space or tab and you can't mix spaces and tabs.


.. _add_category_fields:

add_category_fields
===================

**Usage:** ``./manage.py add_category_fields [app1 app2 ...]``

Add missing registered category fields to the database table of a specified application or all registered applications.

Requires Django South.


.. _drop_category_field:

drop_category_field
===================

**Usage:** ``./manage.py drop_category_field app_name model_name field_name``

Drop the ``field_name`` field from the ``app_name_model_name`` table, if the field is currently registered in ``CATEGORIES_SETTINGS``\ .

Requires Django South.