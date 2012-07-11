=========================
Template tags and filters
=========================

.. contents::
   :depth: 2
   :local:
   :backlinks: top


Filters
=======


``category_path``
-----------------

**Optional Parameter:** separator string. *Default:* ``" :: "``

Creates a path represented by a categories by joining the items with a separator.

Each path item will be coerced to unicode, so you can pass a list of category instances, if required.

**Example using a list of categories:**

.. code-block:: django

   {{ some_list|category_path }}

If ``some_list`` is ``[ <Category: Country>, <Category: Country pop>, <Category: Urban Cowboy>]`` the result will be::

   Country :: Country pop :: Urban Cowboy

**Example using a category node and optional separator parameter:**

.. code-block:: django

   {{ some_node.get_ancestors|category_path:" > " }}

If ``some_node`` was category "Urban Cowboy", the result will be::

   Country > Country pop > Urban Cowboy

.. _tree_info:

``tree_info``
-------------

**Optional Parameter:** ``"ancestors"``

Given a list of categories, it iterates over the list, generating a tuple of the current category and a dict containing information about the tree structure around it, with the following keys:

``'new_level'``
   ``True`` if the current item is the start of a new level in the tree, ``False`` otherwise.

``'closed_levels'``
   A list of levels which end after the current item. This will be an empty list if the next category's level is the same as or greater than the level of the current item.

Provide the optional argument, ``"ancestors"``, to add a list of unicode representations of the ancestors of the current category, in descending order (root node first, immediate parent last), under the key 'ancestors'.

For example: given the sample tree below, the contents of the list which would be available under the 'ancestors' key are given on the right::

   Country             ->  []
      Country pop      ->  [u'Country pop']
         Urban Cowboy  ->  [u'Country', u'Country pop']

Using this filter with unpacking in a {% for %} tag, you should have enough information about the tree structure to create a hierarchical representation of the tree.

.. code-block:: django

   {% for node,structure in objects|tree_info %}
       {% if structure.new_level %}<ul><li>{% else %}</li><li>{% endif %}
       {{ node.name }}
       {% for level in structure.closed_levels %}</li></ul>{% endfor %}
   {% endfor %}

``tree_queryset``
-----------------

Convert a regular category :py:class:`QuerySet` into a new, ordered :py:class:`QuerySet` that includes the categories selected and their ancestors.

This is especially helpful when you have a subset of categories and want to show the hierarchy for all the items.

For example, if we add it to the example for :ref:`tree_info`:

.. code-block:: django

    {% for node,structure in objects|tree_queryset|tree_info %}
        {% if structure.new_level %}<ul><li>{% else %}</li><li>{% endif %}
        {{ node.name }}
        {% for level in structure.closed_levels %}</li></ul>{% endfor %}
    {% endfor %}

A list of unrelated categories such as ``[<Category: Urban cowboy>, <Category: Urban comtemporary>]``, the above template example will output the two categories and their ancestors:

.. code-block:: html

    <ul><li>
    Country
    <ul><li>
    Country pop
    <ul><li>
    Urban cowboy
    </li></ul></li></ul></li></ul>
    <ul><li>
    Rhythm and blues
    <ul><li>
    Urban contemporary
    </li></ul></li></ul>

.. note::
    Categories that have similar ancestors are grouped accordingly. There is no duplication of the ancestor tree.


Inclusion tags
==============

``display_path_as_ul``
----------------------

**Template Rendered:** ``categories/ul_tree.html``

**Syntax 1:** ``{% display_path_as_ul <category_obj> %}``

**Syntax 2:** ``{% display_path_as_ul <path_string>[ using="app.Model"] %}``

Render the category with ancestors, but no children.

Pass either an object that subclasses :py:class:`CategoryBase` or a path string for the category. Add ``using="app.Model"`` to specify which model when using a path string. The default model used is :py:class:`Category`.

**Example, using Category model:**

.. code-block:: django

    {% display_path_as_ul "/Grandparent/Parent" %}

**Example, using custom model:**

.. code-block:: django

    {% display_path_as_ul "/Grandparent/Parent" using="coolapp.MusicGenre" %}

**Example, using an object:**

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


``display_drilldown_as_ul``
---------------------------

**Template rendered:** ``categories/ul_tree.html``

**Syntax 1:** ``{% display_drilldown_as_ul category_obj %}``

**Syntax 2:** ``{% display_drilldown_as_ul "/Grandparent/Parent" [using="app.Model"] %}``

Render the category with ancestors and children.

**Example, using Category model:**

.. code-block:: django

    {% display_drilldown_as_ul "/Grandparent/Parent" %}

**Example, using custom model:**

.. code-block:: django

    {% display_drilldown_as_ul "/Grandparent/Parent" using="coolapp.MusicGenre" %}

**Example, using an object:**

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


``breadcrumbs tag``
-------------------

**Template rendered:** ``categories/breadcrumbs.html``

**Syntax 1:** ``{% breadcrumbs category_obj [separator=" :: "] %}``

**Syntax 2:** ``{% breadcrumbs "/Grandparent/Parent" [separator=" :: "] [using="app.Model"] %}``

Render breadcrumbs for the given path using ``::`` or the given separator.

**Example using Category model:**

.. code-block:: django

	{% breadcrumbs "/Grandparent/Parent" %}

**Example using a custom model:**

.. code-block:: django

  {% breadcrumbs "/Grandparent/Parent" using="coolapp.MusicGenre" %}

**Example using an object:**

.. code-block:: django

	{% breadcrumbs category_obj %}

Returns:

.. code-block:: html

	<a href="/categories/grandparent/">Grandparent</a> / Parent

You can alter the separator used in the template by adding a separator argument:

.. code-block:: django

	{% breadcrumbs category_obj separator=" &gt; " %}

Returns:

.. code-block:: html

	<a href="/categories/grandparent/">Grandparent</a> &gt; Parent


Template Tags
=============

``get_top_level_categories``
----------------------------

Retrieves an alphabetical list of all the categories that have no parents.

Syntax:

.. code-block:: django

    {% get_top_level_categories [using "app.Model"] as categories %}

Returns an list of categories ``[<category>, <category>, <category, ...]``


``get_category_drilldown``
--------------------------

**Syntax 1:** ``{% get_category_drilldown <path_string> [using "app.Model"] as <varname> %}``

**Syntax 2:** ``{% get_category_drilldown <object> as <varname> %}``

Retrieves the specified category, its ancestors and its immediate children as an iterable. Syntax 1 allows for the retrieval of the category object via a slash-delimited path. The optional ``using "app.Model"`` allows you to specify from which model to retrieve the object.

Example:

.. code-block:: django

    {% get_category_drilldown "/Grandparent/Parent" using "family.Member" as family %}

The second syntax uses an instance of any object that subclasses :py:class:`CategoryBase`

.. code-block:: django

    {% get_category_drilldown category_obj as family %}

Both examples sets ``family`` to::

    [Grandparent, Parent, Child 1, Child 2, Child n]

``recursetree``
---------------

This tag renders a section of your template recursively for each node in your
tree.

For example:

.. code-block:: django

    <ul class="root">
        {% recursetree nodes %}
            <li>
                {{ node.name }}
                {% if not node.is_leaf_node %}
                    <ul class="children">
                        {{ children }}
                    </ul>
                {% endif %}
            </li>
        {% endrecursetree %}
    </ul>

Note the special variables ``node`` and ``children``.
These are magically inserted into your context while you're inside the
``recursetree`` tag.

  ``node`` is an instance of your MPTT model.

  ``children`` : This variable holds the rendered HTML for the children of
  ``node``.

.. note::
    If you already have variables called ``node`` or ``children`` in your
    template, and you need to access them inside the ``recursetree`` block,
    you'll need to alias them to some other name first:

    .. code-block:: django

        {% with node as friendly_node %}
            {% recursetree nodes %}
                {{ node.name }} is friends with {{ friendly_node.name }}
                {{ children }}
            {% endrecursetree %}
        {% endwith %}
