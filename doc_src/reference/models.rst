======
Models
======

CategoryBase
============

.. py:class:: CategoryBase

   .. py:attribute:: parent
      
      :py:class:`TreeForeignKey` ``(self)``
      
      The category's parent category. Leave this blank for an root category.
   
   .. py:attribute:: name
      
      **Required** ``CharField(100)``
      
      The name of the category.
   
   .. py:attribute:: slug
      
      **Required** ``SlugField``
      
      URL-friendly title. It is automatically generated from the title.
   
   .. py:attribute:: active
      
      **Required** ``BooleanField`` *default:* ``True``
      
      Is this item active. If it is inactive, all children are set to inactive as well.
   
   .. py:attribute:: objects
      
      ``CategoryManager``
      
      An object manager that adds an ``active`` method for only selecting items whose ``active`` attribute is ``True``.
   
   .. py:attribute:: tree
      
      ``TreeManager``
      
      A Django-MPTT `TreeManager <http://readthedocs.org/docs/django-mptt/en/latest/models.html#the-treemanager-custom-manager>`_ instance.

Category
========

.. py:class:: Category
   
   Category is a subclass of :py:class:`CategoryBase` and includes all its attributes.
   
   .. py:attribute:: thumbnail
      
      ``FileField``
      
      An optional thumbnail, that is uploaded to :ref:`thumbnail_upload_path`  via :ref:`THUMBNAIL_STORAGE`.
      
      .. note:: Why isn't this an ``ImageField``?
         
         For ``ImageField``\ s, Django checks the file system for the existance of the files to handle the height and width. In many cases this can lead to problems and impact performance.
         
         For these reasons, a ``FileField`` that manually manages the width and height was chosen.

   .. py:attribute:: thumbnail_width
      
      ``IntegerField``
      
      The thumbnail width. Automatically set on save if a thumbnail is uploaded.
   
   .. py:attribute:: thumbnail_height
      
      ``IntegerField``
      
      The thumbnail height. Automatically set on save if a thumbnail is uploaded.

   .. py:attribute:: order
      
      **Required** ``IntegerField`` *default:* 0
      
      A manually-managed order of this category in the listing. Items with the same order are sorted alphabetically.

   .. py:attribute:: alternate_title
      
      ``CharField(100)``
      
      An alternative title to use on pages with this category.
   
   .. py:attribute:: alternate_url
      
      ``CharField(200)``
      
      An alternative URL to use instead of the one derived from the category hierarchy.
      
      .. note:: Why isn't this a ``URLField``?
         
         For ``URLField``\ s, Django checks that the URL includes ``http://`` and the site name. This makes it impossible to use relative URLs in that field.

   .. py:attribute:: description
      
      ``TextField``
      
      An optional longer description of the category. Very useful on category landing pages.

   .. py:attribute:: meta_keywords
      
      ``CharField(255)``
      
      Comma-separated keywords for search engines.
   
   .. py:attribute:: meta_extra
      
      ``TextField``
      
      (Advanced) Any additional HTML to be placed verbatim in the ``<head>`` of the page.
