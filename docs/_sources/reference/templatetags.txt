=============
Template Tags
=============

get_top_level_categories
========================

Retrieves an alphabetical list of all the categories that have no parents.

Syntax:

.. code-block:: django

    {% get_top_level_categories as categories %}

Returns an list of categories ``[<category>, <category>, <category, ...]``


display_path_as_ul
==================

Render the category with ancestors, but no children using the ``categories/ul_tree.html`` template.

Example:

.. code-block:: django

    {% display_path_as_ul "/Grandparent/Parent" %}

or

.. code-block:: django

    {% display_path_as_ul category_obj %}

Returns:

.. code-block:: html

	<ul>
	  <li><a href="/categories/">Top</a>
	  <ul>
	    <li><a href="/categories/grandparent/">Grandparent</a></li>
	  </ul>
	  </li>
	</ul>


get_category_drilldown
======================

Retrieves the specified category, its ancestors and its immediate children
as an iterable.

Example:

.. code-block:: django

    {% get_category_drilldown "/Grandparent/Parent" as family %}

or

.. code-block:: django

    {% get_category_drilldown category_obj as family %}

Sets ``family`` to::

    [Grandparent, Parent, Child 1, Child 2, Child n]


display_drilldown_as_ul
=======================

Render the category with ancestors and children using the
``categories/ul_tree.html`` template.

Example:

.. code-block:: django

    {% display_drilldown_as_ul "/Grandparent/Parent" %}

or:

.. code-block:: django

    {% display_drilldown_as_ul category_obj %}

Returns:

.. code-block:: html

    <ul>
      <li><a href="/categories/">Top</a>
      <ul>
        <li><a href="/categories/grandparent/">Grandparent</a>
        <ul>
          <li><a href="/categories/grandparent/parent/">Parent</a>
          <ul>
            <li><a href="/categories/grandparent/parent/child1">Child1</a></li>
            <li><a href="/categories/grandparent/parent/child2">Child2</a></li>
            <li><a href="/categories/grandparent/parent/child3">Child3</a></li>
          </ul>
          </li>
        </ul>
        </li>
      </ul>
      </li>
    </ul>


breadcrumbs tag
===============

Render breadcrumbs, using the ``categories/breadcrumbs.html`` template, using the optional ``separator`` argument.

Example:

.. code-block:: django

	{% breadcrumbs "/Grandparent/Parent" %}

or:

.. code-block:: django

	{% breadcrumbs category_obj %}

Returns:

.. code-block:: html

	<a href="/categories/grandparent/">Grandparent</a> / Parent

You can alter the separator used in the template by adding a string argument to be the separator:

.. code-block:: django

	{% breadcrumbs category_obj "::" %}

Returns:

.. code-block:: html

	<a href="/categories/grandparent/">Grandparent</a> :: Parent
