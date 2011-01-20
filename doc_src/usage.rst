=============================
Using categories in templates
=============================

To use the template tags:::

	{% import category_tags %}

Filters
*******

``tree_info``
-------------

Given a list of categories, iterates over the list, generating
two-tuples of the current tree item and a ``dict`` containing
information about the tree structure around the item, with the following
keys:

   ``'new_level'``
      ``True`` if the current item is the start of a new level in
      the tree, ``False`` otherwise.

   ``'closed_levels'``
      A list of levels which end after the current item. This will
      be an empty list if the next item's level is the same as or
      greater than the level of the current item.

An optional argument can be provided to specify extra details about the
structure which should appear in the ``dict``. This should be a
comma-separated list of feature names. The valid feature names are:

   ancestors
      Adds a list of unicode representations of the ancestors of the
      current node, in descending order (root node first, immediate
      parent last), under the key ``'ancestors'``.

      For example: given the sample tree below, the contents of the list
      which would be available under the ``'ancestors'`` key are given
      on the right::

         Books                    ->  []
            Sci-fi                ->  [u'Books']
               Dystopian Futures  ->  [u'Books', u'Sci-fi']