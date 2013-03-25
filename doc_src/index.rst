=============================
Django Categories v |version|
=============================

Django Categories grew out of our need to provide a basic hierarchical taxonomy management system that multiple applications could use independently or in concert.

As a news site, our stories, photos, and other content get divided into "sections" and we wanted all the apps to use the same set of sections. As our needs grew, the Django Categories grew in the functionality it gave to category handling within web pages.

New in 1.1
==========

* Fixed a cosmetic bug in the Django 1.4 admin. Action checkboxes now only appear once.

* Template tags are refactored to allow easy use of any model derived from ``CategoryBase``.

* Improved test suite.

* Improved some of the documentation.



Contents
========

.. toctree::
   :maxdepth: 2
   :glob:

   installation
   getting_started
   usage
   registering_models
   adding_the_fields
   admin_settings
   custom_categories
   reference/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

