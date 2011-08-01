.. _adding_the_fields:

=================================
Adding the fields to the database
=================================

While Django will create the appropriate columns and tables if you configure Django Categories first, many times that is not possible. You could also reset the table, but you would loose all data in it. There is another way.

Enter South
***********

`South <http://south.aeracode.org/>`_ is a Django application for managing database schema changes. South's default behavior is for managing permanent changes to a model's structure. In the case of dynamically adding a field or fields to a model, this doesn't work because you are not making the change permanent. And probably don't want to.

Django Categories has a management command to create any missing fields. It requires South because it uses the South's API for making changes to databases. The management command is simple: ``python manage.py add_category_fields [app]``\ . If you do not include an app name, it will attempt to do all applications configured.

Running this command several times will not hurt any data or cause any errors.

Reconfiguring Fields
********************

You can make changes to the field configurations as long as they do not change the underlying database structure. For example, adding a ``related_name`` (see :ref:`registering_a_m2one_relationship`\ ) because it only affects Django code. Changing the name of the field, however, is a different matter.

Django Categories provides a complementary management command to drop a field from the database (the field must still be in the configuration to do so): ``python manage.py drop_category_field app_name model_name field_name``