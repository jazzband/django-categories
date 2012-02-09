.. _creating_custom_categories:

==========================
Creating Custom Categories
==========================

Django Categories isn't just for using a single category model. It allows you to create your own custom category-like models with as little or much customization as you need.

Name only
=========

For many cases, you want a simple user-managed lookup table. You can do this with just a little bit of code. The resulting model will include name, slug and active fields and a hierarchical admin.

#. Create a model that subclasses :py:class:`CategoryBase`

   .. literalinclude:: code_examples/custom_categories1.py
      :linenos:

#. Create a subclass of CategoryBaseAdmin.

   .. literalinclude:: code_examples/custom_categories1.py
      :linenos:

#. Register your model and custom model admin class.

Name and other data
===================

Sometimes you need more functionality, such as extra metadata and custom functions. The :py:class:`Category` model in this package does this.

#. Create a model that subclasses :py:class:`CategoryBase` as above.

#. Add new fields to the model. The :py:class:`Category` model adds these extra fields.

   .. literalinclude:: code_examples/custom_categories3.py
      :linenos:

#. Add new methods to the model. For example, the :py:class:`Category` model adds several new methods, including overriding the :py:meth:`save` method.

   .. literalinclude:: code_examples/custom_categories4.py
      :linenos:

#. Alter :py:class:`Meta` or :py:class:`MPTTMeta` class. Either of these inner classes can be overridden, however your :py:class:`Meta` class should inherit :py:class:`CategoryBase.Meta`. Options for :py:class:`Meta` are in the `Django-MPTT docs <http://readthedocs.org/docs/django-mptt/en/latest/models.html#model-options>`_.

   .. literalinclude:: code_examples/custom_categories5.py
      :linenos:

#. For the admin, you must create a form that subclasses :py:class:`CategoryBaseAdminForm` and at least sets the ``Meta.model`` attribute. You can also alter the form fields and cleaning methods, as :py:class:`Category` does.

   .. literalinclude:: code_examples/custom_categories6.py
      :linenos:

#. Next you must subclass :py:class:`CategoryBaseAdmin` and assign the ``form`` attribute the form class created above. You can alter any other attributes as necessary.

   .. literalinclude:: code_examples/custom_categories7.py
      :linenos:
