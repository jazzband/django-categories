# Changelog


## Unreleased (2021-12-05)

### New

* Added pre-commit configuration and configuration for the tools. [Corey Oordt]

* Added XML reporting for code coverage. #164. [Corey Oordt]

* Added codecov uploading to Tox. #164. [Corey Oordt]

* Adds GitHub Actions to run Tox. #164. [Corey Oordt]

* Added contributing documentation. #164. [Corey Oordt]

* Added Jazzband badge to README. [Corey Oordt]

  Also changed it to Markdown.

### Updates

* Changed codecov uploading pattern. [Corey Oordt]

* Updated tox to run coverage commands together. [Corey Oordt]

* Updated references to Python 3.10. #164. [Corey Oordt]

* Updated gitignore to be more ignorative. [Corey Oordt]

* Updates URL of the project to Jazzband. #164. [Corey Oordt]

### Other

* Removed Python 3.10 testing until compatibility established. [Corey Oordt]


## 1.8.0 (2020-08-31)

### New

* Add support for Django 3.1. [gantonayde]

  In Django 3.1 the compatibility import of django.core.exceptions.FieldDoesNotExist in django.db.models.fields is removed.

  So we'd have to update the package by replacing:
  from django.db.models.fields import FieldDoesNotExist
  with
  from django.core.exceptions import FieldDoesNotExist

### Updates

* Update the version to 1.8. [Brent O'Connor]

* Update tox tests to run Django 3.1 and removed support for Python 2.7. [Brent O'Connor]

### Other

* Remove Python 2.7 from the Travis config. [Brent O'Connor]

* Django-mptt 0.11 needed for Django 3.1. [gantonayde]

  In Django 3.1 the compatibility import of django.core.exceptions.FieldDoesNotExist in django.db.models.fields is removed.
  django-mptt should be the latest version (0.11 as of now)


## 1.7.2 (2020-05-18)

### Updates

* Update publish make task. [Brent O'Connor]

### Fix

* Fix #152. [Petr Dlouhý]

### Other

* Include missing migration. [Carlos Cesar Caballero Díaz]

* Ignore .python-version. [Brent O'Connor]


## 1.7.1 (2020-03-06)

### New

* Add missing migrations. [Brent O'Connor]


## 1.7.0 (2020-02-04)

### New

* Add newer Django versions to tox.ini. [Petr Dlouhý]

### Updates

* Update django-mptt. [Petr Dlouhý]

* Update `make publish` [Brent O'Connor]

### Fix

* Fixes to Django 3.0. [Petr Dlouhý]


## 1.6.1 (2019-06-26)

### New

* Adding opts to context for Django version 2 and above. [Gagandeep Singh]

* Django 2.0 support in Admin. [Gagandeep Singh]

  TypeError at /admin/categories/category/
  __init__() missing 1 required positional argument: 'sortable_by'

### Updates

* Update Travis. [Brent O'Connor]

   * travis.yml
   * build badge
   * Remove 3.7 from Travis config since it doesn't look like it's supported
   * Switch to tox-travis.
   
* Updated tree editor for typo. [Gagandeep Singh]

* Upgrade build environment to Xenial. [Brent O'Connor]

  This makes it so Django 2.2 tests should pass

### Fix

* Fix Travis so it uses the correct python versions. [Brent O'Connor]

* Fix Travis so it works with Python 3.7. [Brent O'Connor]

* Fix 'Models aren't loaded yet' warning on import. [Frankie Dintino]

  categories.registration._process_registry was being called in
  categories/__init__.py, but since Django 1.9 it hasn't been possible to
  perform operations with models until the app registry is fully
  loaded. Currently the `AppRegistryNotReady` exception is being caught
  and printed, which means it is never actually executed on load.

  Since this code isn't currently doing anything (other than emitting a
  print() of a warning), I've removed it.

* Fix tests. [Brent O'Connor]

  Also dropped testing Django 1.10 since django-mptt requires Django>=1.11.

* Fix for TOXENV=py27-lint. [Gagandeep Singh]

* Fixing model for TOXENV=py36-django110. [Gagandeep Singh]

* Py27-lint test fix. [Gagandeep Singh]

* Test Cases fix. [Gagandeep Singh]

* Bug Fix : sortable was last argument. [Gagandeep Singh]



## 1.6.0 (2018-02-27)

### Updates

* Updated the Travis CI config. [Brent O'Connor]

* Changed from using a string to importing the actual CASCADE function. [Brent O'Connor]

### Other

* Proposes changes based on 366ff74619811505ac73ac5ea2c0096ddab0ac51 and pull request #140 for Django 2.0 to pass CI tests. [goetzb]

* Made updates to get everything working with Django 2. [Brent O'Connor]


## 1.5.4 (2017-10-13)

### New

* Django 1.11 compatibility. [Hodossy Szabolcs]

* Support Django 1.11 testing environment. [Egor]

* Add migrations for simpletext example app. [Corey Oordt]

### Fix

* Fix changlist TypeError. Return RequestContext as dict on changelist_view. [Egor]

   * Based on [changes in Django 1.11](https://docs.djangoproject.com/en/1.11/releases/1.11/#django-template-backends-django-template-render-prohibits-non-dict-context)

* Get management commands compatible with Django 1.10+ [Corey Oordt]

### Updates

* Updated test settings to test generic relations. [Corey Oordt]

* Updated tox and travis configurations to check py2.7 and 3.6 and django 1.8-1.11. [Corey Oordt]


### Other

* Made sure example was excluded from packaging. [Corey Oordt]

* Remove old django-cbv reference and adds better error checking in views. [Corey Oordt]

* Retrieve content types lazily in Generic Relations admin. [Corey Oordt]

* Check for a valid session id before trying to save or rollback a transaction. [Corey Oordt]

* Added additional test coverage for management commands and views. [Corey Oordt]

* Remove south migrations. [Corey Oordt]

* Set decendent_ids to empty list if not saved. [Corey Oordt]

* Removing every occurrence of Requestcontext and Context. [Hodossy Szabolcs]


## 1.5.3 (2017-03-31)

### Fix

* Fixed a ValueError that happened when trying to save a Category that has a thumbnail. [Brent O'Connor]

### Other

* Version bump. [Brent O'Connor]


## 1.5.2 (2017-03-29)

### Fix

* Fixed a unicode error that happens with Python 2.7. [Brent O'Connor]


## 1.5.1 (2017-02-17)

### New

* Added a missing migration. [Brent O'Connor]

### Updates

* Updated README.rst with svg badge. [Sobolev Nikita]

### Fix

* Close table tag in templatetag result. [Dheeraj Sayala]

  In items_for_tree_result, there's a format_html call which builds HTML via string interpolation. It missed back slash in the closing tag. This commit adds that.

### Other

* Just to be safe - pin it down. [Primož Verdnik]


## 1.5 (2016-11-14)

### Updates

* Updated the Travis config to test for Django 1.10. [Brent O'Connor]

* Updated django-categories to work with Django 1.10. [Brent O'Connor]


## 1.4.3 (2016-10-21)

### Fix

* Fixes popup raw_id fields for django versions 8 or greater. [Jordan Roth]


## 1.4.2 (2016-04-19)

### Fix

* Fixed it so display_for_field works with Django 1.8 and 1.9. [Brent O'Connor]


## 1.4.1 (2016-03-31)

### New

* Added setup.cfg file for creating universal wheel distribution. [Brent O'Connor]

* Added coverage to tox. [Brent O'Connor]

* Added some tests to test the admin. [Brent O'Connor]

* Added a makefile for common tasks. [Brent O'Connor]

### Updates

* Updated the new in 1.4 information. [Brent O'Connor]

### Fix

* Fixed an exception error that happens when saving a category in the admin. [msaelices]

* Removed some RemovedInDjango110Warning warnings. [Brent O'Connor]

### Other

* Moved all template settings for the example app into the TEMPLATES Django setting. [Brent O'Connor]

* Avoid the "Cannot call get_descendants on unsaved Category instances" ValueError when adding categories in admin interface. [msaelices]

* Removed contributors from the README since that information is in CREDITS.md. No sense maintaining it two places. [Brent O'Connor]


## 1.4 (2016-02-15)

### New

* Added a tox.ini and updated the travis config to work with tox. [Brent O'Connor]

### Updates

* Updated admin_tree_list_tags so that EMPTY_CHANGELIST_VALUE has a compatible way of working with Django 1.9 and older versions. [Brent O'Connor]

* Updated urls to work without patterns since patterns is being deprecated. [Brent O'Connor]

* Updated settings to remove all the TEMPLATE_* settings and put them into the TEMPLATES dict for Django 1.9 compatibility. [Brent O'Connor]

* Changed __unicode__ to __str__ on the CategoryBase class for Python 3 compatibility. [Brent O'Connor]

* Upgraded to django-mptt 0.8. [Brent O'Connor]

* Switched to using _meta.get_fields() instead of ._meta.get_all_field_names() for compatibility with Django 1.9. [Brent O'Connor]

* Replaced django.db.models.get_model with django.apps.apps.get_model for future compatibility with Django. [Brent O'Connor]

* Switched to importing the correct templatetags that got renamed. [Brent O'Connor]

* Switched form using smart_unicode to smart_text and force_unicode to force_text. [Brent O'Connor]

* Switched from using django.db.models.loading.get_model to using django.apps.apps.get_model. [Brent O'Connor]

* Switched form using force_unicode to force_text. [Brent O'Connor]

* Use singleton `registry` to import `register_fk` and `register_m2m` since they are members on `Registry` class. [Orestes Sanchez]

### Fix

* Fixed the max_length setting to use a int instead of a string. [Brent O'Connor]

* Fixed a test: file() doesn't work in Python 3, used open() instead. [Brent O'Connor]

* Made a bunch of flake8 fixes and also added flake8 testing to Travis and Tox. [Brent O'Connor]

* Made a fix for backwards compatibility with Python 2. [Brent O'Connor]

* B'' doesn't work under Python 3 in a migration file. [Brent O'Connor]

### Other

* Ran the 2to3 script `2to3 -w .` [Brent O'Connor]

* Ugettext may cause circular import. [Basile LEGAL]

* Run the test with a different configuration. [Orestes Sanchez]


## 1.3 (2015-06-09)

### New

* Added the fields property with it set to '__all__' in order to not get the RemovedInDjango18Warning. [Brent O'Connor]

* Defaulting the url prefix to / if it can't find the category tree. [Corey Oordt]

* I18n: add french translation. [Olivier Le Brouster]

### Updates

* Updates the existing migration to south_migrations. [Corey Oordt]

* Renamed get_query_set to get_queryset to get Django categories to work in Django 1.7. I'm not sure of a good way to make this work in Django 1.6. [Brent O'Connor]

* Migrations
  
   * Dramatically refactored how migrations are performed to work with Django 1.7. [Corey Oordt]

   * Missed some migrations. [Jose Soares]

   * Changing migration dependency of contenttypes to 0001_initial for support for Django 1.7. [Corey Oordt]

### Fix

* Fixes potential double imports in dev and test servers. [Corey Oordt]

* Fixed a potential issue with double-loading of the dev server. [Corey Oordt]

* Fixes a conflict with treebeard. They stole the name admin_tree_list. [Corey Oordt]

* Fixed the RemovedInDjango19Warning deprecation warning. [Brent O'Connor]

* Fixed tests so they run under Django 1.7. [Brent O'Connor]

* fixes registration when there is no app config. [Corey Oordt]

* [-] Fixed some tree editor and generic collection issues. [Jose Soares]

### Other

* Removing outdated settings and updating outdated files. [Corey Oordt]

* [-] 1.6/1.7/1.8 compatiable changes (WIP) [Jose Soares]


## 1.2.3 (2015-05-05)

### New

* Added a new way to register models manually. [Corey Oordt]

* Bootstrap class on table (important for django-suit) [Mirza Delic]

### Updates

* Update requirements. [Sina Samavati]

* Using custom model in CategoryDetailView. [Enver Bisevac]

### Fix

* Fix unicode slug issue. [Sina Samavati]


## 1.2.2 (2013-07-07)

### New

* Italian localization. [Iacopo Spalletti]

### Fix

* Fixing migration script for adding fields. [Corey Oordt]

* Fixed i18n and failing test in Django 1.4. [Corey Oordt]

### Other

* Load I18N templatetags. [Eugene]


## 1.2.1 (2013-03-22)

### Fix

* Fixed i18n and failing test in Django 1.4. [Corey Oordt]


## 1.2 (2013-03-20)

### New

* Added admin settings documentation. [Corey Oordt]

* Added customization of admin fieldsets. [Corey Oordt]

### Updates

* Update categories/templatetags/category_tags.py. [Glen]

  * Added NoneType check to display_drilldown_as_ul on line 188 to fix NoneType error.

  * Added str() to line 49 to fix an error where .strip("'\"") in get_category is getting called on a non-string category_string.
  
* Made updates so django-categories works with django-grappelli. [Brent O'Connor]

* Updated the code so it will work with or without Grappelli installed. [Brent O'Connor]

### Fix

* Fixing a few minor Django 1.5 incompatibilities. [Corey Oordt]

* Fix for Django 1.5: {% url %} parameter needs to be quoted. [Corey Oordt]

* Fixed an exception error. [Brent O'Connor]

  Fixed an exception error that occurs when an empty form is submitted for apps that are created using categories.base.CategoryBase.

### Other

* Version bump 1.2. [Corey Oordt]

* Updating the admin template to support the latest django admin code. [Corey Oordt]

* I18n. [winniehell]

* German translation. [winniehell]

* 1.5 compat: remove adminmedia templatetag calls. [Yohan Boniface]

  See https://docs.djangoproject.com/en/1.5/releases/1.5/#miscellaneous

* Made it so django-categories works with Django 1.5 and Grappelli 2.4.4. [Brent O'Connor]

* Simplified the assignment of the IS_GRAPPELLI_INSTALLED variable. [Brent O'Connor]



## 1.1.3 (2012-08-29)

### Other

* To satisfy a very demanding and owly jsoa, I removed an unused variable. :P. [Corey Oordt]

* Updating the signal registration to check for south first and fail silently. [Corey Oordt]

* Moved the registration of the signal to models.py where it will get executed. [Corey Oordt]

* Refactored the migration script to use the syncdb signal. The post_migrate signal only fires for south-managed apps, so it isn't as useful. [Corey Oordt]


## 1.1.2 (2012-08-18)

### New

* Added travisci. [Jose Soares]

### Fix

* Fixed a bug in the compatibility layer. [Corey Oordt]

* Minor tweak to tempatetag tests. [Jose Soares]

### Other

* Can't use the m2m tests because it conflicts with the fk tests. [Corey Oordt]

* Placing some south imports into try blocks. [Corey Oordt]

* Capitalizing the various REGISTRY settings. [Corey Oordt]

* Refactored the registration of fields from __init__ to a new module. [Corey Oordt]

  It also makes it easier to test.


## 1.1 (2012-07-12)

### New

* Added Brad Jasper to the credits and updated Jonathan's github account. [Corey Oordt]

* Added queryset parameter to ChangeList.get_ordering() [Brad Jasper]

### Updates

* Updated read me and version bump to 1.1. [Corey Oordt]

* Updated and rendered docs. [Corey Oordt]

* Update to template tags to include ways to retrieve an object from a model other than Category. [Corey Oordt]

* Updated the credits to add Iacopo Spalletti. [Corey Oordt]

* Updated CREDITS, docs. [Jose Soares]

### Fix

* Fixed an incorrect include in the example. [Corey Oordt]

* Fixed some Django 1.4 cosmetic issues. [Corey Oordt]

* Fixes Pull Request #37 Adds notification in the readme regarding issue with South version 0.7.4. [Corey Oordt]

* Fixed format error. [Iacopo Spalletti]

* Fixes issue #40 Checks for instance of CategoryBase instead of Category. [Corey Oordt]

  There are still some template tags that won't work with subclasses. Need a better solution for those tags.

### Other

* Template tags now work with any derivative of CategoryBase. Recognizes the "using" param to specify the model to use. [Corey Oordt]

* Sorry, typo in documentation. [Iacopo Spalletti]

* Documented the upgrade path from 1.0.2 and 1.0.3 plus a small migration to keep things in sync. [Iacopo Spalletti]

* Stylistic fixes and docs. [Martin Matusiak]

* Make it optional to register in admin. [Martin Matusiak]

* Use ugettext_lazy. [Martin Matusiak]

* Minor fix to example app. [Jose Soares]


## 1.0.3 (2012-03-28)

### New

* Adding additional migrations to fix potential data corruption when renaming the foreign key. [Corey Oordt]

### Fix

* Fixed another migration. [Corey Oordt]

* Altering the #10 migration as it caused strange behavior with data. [Corey Oordt]


## 1.0.1 (2012-03-09)

### Other

* Importing get_model directly from the loading module appears to fix certain edge cases. [Corey Oordt]


## 1.0.2 (2012-03-06)

### Fix

* Fixed how the activate/deactivate methods in the admin fetched their models. [Corey Oordt]

* Fix for django 1.4 compatibility. [Corey Oordt]

### Other

* Removed an errant print statement. [Corey Oordt]


## 1.0 (2012-02-15)

### New

* Added compatibility with Django 1.4. [Corey Oordt]

* Allow the setting of a SLUG_TRANSLITERATOR to convert non-ASCII characters to ASCII characters. [Corey Oordt]

### Updates

* Updated documentation for 1.0b1. [Corey Oordt]

* Updated migrations to include a data migration. [Corey Oordt]

* Updated the default view caching to 600, which is the django default instead of forcing the views to NEVER cache at all. [Corey Oordt]

* Updating docs to correct and simplify the simple custom categories instructions. [Corey Oordt]

### Fix

* Also fixes #30 by including the editor's media. [Corey Oordt]

* Formally fixes #1 by adding the ability to specify a transliteration function. [Corey Oordt]

* Addresses issue #27; updated musicgenres.json. [Jose Soares]

* The admin prior to 1.4 requires a different result from get_ordering. [Corey Oordt]

* This fixes #31. [Corey Oordt]

  * Uses the incorrect version segment. Although it works in 1.4a1, it is not perfect.

### Other

* Removed the __init__ method for the treechange list. Don't need it and it varies too much by django version. [Corey Oordt]


* Test of the CategoryBase class subclassed without extras. [Corey Oordt]

* Moved the base models to base.py and did a few PEP8 cleanups. [Corey Oordt]

* Moved the base classes to a new file to isolate them. [Corey Oordt]

* Refactored the admin into a base class for subclasses. [Corey Oordt]

* Extracted a base class for categories to allow other apps to make their own independent category-style models. [Corey Oordt]

  * Updated for django-mptt 0.5.2
  * Fixed typo in the CategoryRelation field in that the foreign key is called 'story'
  * Made the order field non-null and default to 0
  * Changed the parent foreign key a TreeForeignKey (for 0.5.2)
  * Changed requirements to mptt>=0.5.2
  * Added a migration for model changes.


## 0.8.9 (2012-02-06)

### Updates

* Updated the docs. [Jose Soares]

### Fix

* Fixes issue #30; includes static directory when packaged. [Jose Soares]

### Other

* Moved the editor app so it's inside the categories app. [Jose Soares]


## 0.8.7 (2012-01-05)

### Updates

* Changed behavior of (de)activating an item within the change form: [Corey Oordt]

  Instead of changing all descendants' active status to the current item's, it will only change the descendants' active status if the item is False.

  As it makes sense to have an item active, but its children inactive, it doesn't make sense that an item is inactive, but its descendants are active.

  This doesn't change the activate/deactivate admin actions. They will always  affect an item and its descendants.


## 0.8.6 (2012-01-03)

### New

* Added a django/jQuery stub for previous versions of Django. [Corey Oordt]

* Added David Charbonnier to the credits. [Corey Oordt]

### Fix

* Fixes #13 : Documented installation and re-rendered the docs. [Corey Oordt]

* Fix missing imports. [David Charbonnier]

### Other

* Altered the field type of the alternate url field from URL to Char. This allows relative urls, instead of full urls. [Corey Oordt]

  Added a migration in case the database complains. Really doesn't do anything on that level


## 0.8.5 (2011-11-03)

### Fix

* Fixes issue #26 by limiting the slug to the first 50 characters. [Corey Oordt]


## 0.8.4 (2011-10-14)

### New

* Added a version check to support Django 1.1 in a core Django function. [Corey Oordt]


## 0.8.3 (2011-10-13)

### Other

* Activate and Deactivate of a child no longer (de)activates their parent. [Corey Oordt]

  The query set includes the entire hierarchy. So manually get the categories based on the selected items. Then do them and their children

* Remove the delete action from the available actions. [Corey Oordt]


## 0.8.2 (2011-09-04)

### Updates

* Updated docs adding usage in templates and rendered. [Corey Oordt]

### Fix

* Fix Issue #25 : The override of __getitem__ was causing issues with analysis of query sets, [Corey Oordt]


## 0.8.1 (2011-08-29)

### Fix

* Fixes a bug trying to set active on decendants before object is saved. [Corey Oordt]


## 0.8 (2011-08-22)

### New

* Added to the README. [Corey Oordt]

* Added an active flag for models. [Corey Oordt]

### Other

* Improved Category import. [Corey Oordt]


## 0.7.2 (2011-08-19)

### New

* Added a check in migrate_app to see if the app is a string or not. [Corey Oordt]

### Updates

* Updated the get_version function to be PEP 386 compliant. [Corey Oordt]

* Changed the DatabaseError import to be more compatible. [Corey Oordt]

* Updated the readme. [Corey Oordt]

### Other

* Pruning the example project. [Corey Oordt]

* Refactored the editor to become Django 1.1.1 compatible and some PEP8 formatting. [Corey Oordt]

* Ensure that the slug is always within the 50 characters it needs to be. [Corey Oordt]


## 0.7.1 (2011-08-03)

### Other

* Due to settings, the migration for the category relations table never would be created. This fixes it. [Corey Oordt]


## 0.7 (2011-08-02)

### New

* Added a setting for the JAVASCRIPT_URL to make placement of the genericcollections.js file easier. [Corey Oordt]

* Added compatibility with Django 1.1 by adding missing methods for editor and bumped version to 0.7beta2. [Corey Oordt]

* Added a get_latest_objects_by_category template tag. Might be useful. [Corey Oordt]

* Added the ability to add the appropriate fields to a table if configured after an initial syncdb. [Corey Oordt]

* Added an alternate url field to the model. [Corey Oordt]

* Added the alternate_url to the admin. [Corey Oordt]

### Updates

* Updated and rendered docs. [Corey Oordt]

* Updated the gitignore for venv file. [Corey Oordt]

* Altered the inline template to display the content_object instead of the __unicode__ of the middle table. [Corey Oordt]

* Updating the documentation. [Corey Oordt]

### Fix

* Fixed a typo in the docs. [Corey Oordt]

* [Fixes issue #23] Changes the way the tree shows items when searched. Doesn't hide them in the template. [Corey Oordt]

* Fixed a bug in the javascript. [Corey Oordt]

### Other

* Refactored the registry into a registry of models and fields. This will make it easier for migrations. [Corey Oordt]

* Deleted old migration scripts since they were migrated to south. [Corey Oordt]


## 0.6 (2011-05-18)

### New

* Added a Deprecation warning for CATEGORIES_RELATION_MODELS. [Corey Oordt]

* Adding South migrations. [Corey Oordt]

* Added some specialized functions for relations. [Corey Oordt]

* Added a class based view for the detail page of a model related to a category. [Erik Simmler]

* Added a view that list items of specific model that are related to the current category. [Erik Simmler]

* Added a class based CategoryDetailView that should be functionally identical to the original function based view. [Erik Simmler]

* Add optional thumbnail model field. [Evan Culver]

### Updates

* Updated docs. [Corey Oordt]

* Updated README. [Corey Oordt]

* Updated some of the setup info. [Corey Oordt]

### Fix

* Fixed a problem in the new admin creation where it wouldn't properly filter out the category fields by model. [Corey Oordt]

* [FIXED Issue #17] Refactored how the HTML is rendered, removing the checkbox from the <a> tag and pulling the parent checkbox from the row class. [Corey Oordt]

* Fixed the deprecated settings in the example app. [Corey Oordt]

* Fixed small errors in templatetags documentation and docstrings. [Ramiro Morales]

* Fixed wrong var name in import_categories command. [Andrzej Herok]

* Fixed the homepage in the setup.py. [Corey Oordt]

### Other

* Final doc rendering. [Corey Oordt]

* Enabled new registry in the example app for testing. [Corey Oordt]

* The registry default settings needs to be an empty dict, not list. [Corey Oordt]

* Enable registering of models in settings. [Corey Oordt]

* Putting registry outside of the try block. [Corey Oordt]

* Updating settings for Django 1.3. [Corey Oordt]

* Refactored the thumbnail from imagefield to filefield. [Corey Oordt]

  Why? ImageField causes hits to storage to fill out certain fields. Added a storage class and width/height fields so it is possible to scale the thumbnails and store them somewhere besides the filesystem.

* Allow for using django-cbv in Django 1.2.x. [Corey Oordt]

* Slight refactor of the default settings to clean it up. [Corey Oordt]

* Filled out all contributors. [Corey Oordt]

* Moved path to category code into its own function to make reuse easier. [Erik Simmler]

* Remove 'to' from kwargs in CategoryM2MField and CategoryFKField. 'to' is already specified, and causes errors when running unit tests. [Martin Ogden]

* Make admin js relative to MEDIA_URL. [Evan Culver]

* Make the initial state of the editor tree an app setting with collapsed as the default. [Erik Simmler]


## 0.5.2 (2011-02-14)

### Other

* Removed the raising of an exception when it finds a model that is already registered. [Corey Oordt]


## 0.5.1 (2011-02-14)

### Updates

* Updated the test to test a new template tag, not the old one. [Corey Oordt]

* Changed the import to import from category_import. [Corey Oordt]

### Other

* The test for importing checks the first child. With two children either could be 1st, so remove one. [Corey Oordt]

* Need to delete all the objects before each test because the import checks its work. [Corey Oordt]

* Checking for raising the correct exception and moved the strings used in the test to a list of strings. [Corey Oordt]

* Got rid of the debugging print statements. [Corey Oordt]


## 0.5 (2011-01-20)

### New

* Added contributors to the readme for proper recognition. [Corey Oordt]

* Added logic to skip adding categories that are already defined for a modeladmin. [Erik Simmler]

* Added additional fields to the display_list. [Corey Oordt]

* Adding a new import and alphabetizing them (OCD, I know) [Corey Oordt]

* Added a new template tag to override the painting of the admin rows. [Corey Oordt]

* New template and media. [Corey Oordt]

* Added a placeholder for Django. [Corey Oordt]

* Adding a new version of TreeTable with a few minor changes to support row repainting. [Corey Oordt]

### Updates

* Updated the documentation! [Corey Oordt]

* Updated the docstrings of the template tags and added breadcrumbs. [Corey Oordt]

### Other

* STATIC_URL seems to be returning as None even when not defined. [Erik Simmler]

* Renamed 'media' directories to 'static' to work with the django 1.3 staticfiles app. [Erik Simmler]

* Removed duplicate slash from EDITOR_MEDIA_PATH setting. [Erik Simmler]

* ModelAdmin re-register now skips modeladmins without fieldsets already defined. [Erik Simmler]

  Was causing a "TypeError at /current/url/: unsupported operand type(s) for +: 'NoneType' and 'tuple'"

* Got rid of the with_stories keyword for the category detail view. [Corey Oordt]

* Revised the README to get it up-to-date. [Corey Oordt]

* Refactored the templates to extend a categories/base.html. [Corey Oordt]

* Renamed the README to indicate it is a reST file. [Corey Oordt]

* Long trees cause a performance hit if the initial state is expanded. Changing to "collapsed" [Corey Oordt]

* Getting rid of unused code in the treeeditor. [Corey Oordt]

* Ignoring a few more things. [Corey Oordt]

* Made the media delivery work. [Corey Oordt]

* Removed some unused cruft from the TreeEditor class. [Corey Oordt]

* What's that doing there? [Corey Oordt]

* Now that Django has a getchangelist function, we don't need to hack anymore. [Corey Oordt]

* Don't need to set that EDITOR_MEDIA_PATH any more. [Corey Oordt]

* Reworked the template to initialize the correct javascript and use the result_tree_list. [Corey Oordt]

* Deleted an unused template. [Corey Oordt]

* Got rid of hotlinking settings and changed the EDITOR_MEDIA_PATH. [Corey Oordt]

* Removed unused code files. [Corey Oordt]

* Removed all the old, unused templates. [Corey Oordt]

* Removed all the old media. [Corey Oordt]



## 0.4.8 (2010-12-10)

### New

* Added a Meta class for proper plural naming. [Corey Oordt]

### Updates

* Updated the requirements to django-mptt 0.4.2. [Corey Oordt]
* Modified Category model to work with django-mptt 0.4. [Josh Ourisman]

### Fix

* Fixing bug #6 per primski. Adds the correct fields into the admin instead of both. [Corey Oordt]

### Other

* PyPI didn't like the license metadata. [Corey Oordt]


## 0.4.6 (2010-10-07)

### Other

* Bumped version to 0.4.6. [Corey Oordt]


## 0.4.5 (2010-10-07)

### Fix

* Fix fieldsets assignment, issue 3. [Justin Quick]

* Category string, fixes issue 2. [Justin Quick]

### Other

* Checks for parent if given enough path bits. [Justin Quick]


## 0.4.4 (2010-05-28)

### New

* Added the extra templates. [Corey Oordt]

* Added extra context to view func. [Justin Quick]

### Other

* Redid docs with new template. [Corey Oordt]

* Refactoring docs into doc_src and docs. [Corey Oordt]

* Require a trailing slash at the end of urls. [Corey Oordt]

* Safe mptt registration. [Justin Quick]


## 0.4.2 (2010-04-28)

### Updates

* Updated the version number. [Corey Oordt]

### Fix

* Fixing jquery issues. [Corey Oordt]

### Other

* Fied my typo for settings url. [Web Development]


## 0.4 (2010-04-23)

### New

* Added the necessary files to test the generic relations. [Corey Oordt]

* Added generic relation stuff into categories. [Corey Oordt]

### Other

* Renamed sample to example because that is what every other one is called, damnit. [Corey Oordt]


## 0.3 (2010-04-23)

### New

* Added metadata to the model for seo stuff. [Corey Oordt]

### Updates

* Changed the requirements from mptt in our repository to mptt-2 in pypi. [Corey Oordt]


## 0.2.2 (2010-04-08)

### New

* Added better setup.py pieces. Getting ready to push to our PyPi. [Corey Oordt]

### Updates

* Changed the requirements to have mptt just greater than 0.2. [Corey Oordt]

### Other

* Switched to setuptools/distribute. [Corey Oordt]

* Deleted code referencing something I deleted earlier. [Corey Oordt]

* Removing docs for piece I deleted previously. [Corey Oordt]



## 0.2.1 (2010-04-06)

### New

- Added some docs and testing apps. [Corey Oordt]
- Added a caching setting to vary the amount of time the view is cached.
  [Corey Oordt]
- Added missing templates for category traversal. [Justin Quick]
- Added an app to test categories against. [Corey Oordt]
- Added some registration notes to start the docs. [Corey Oordt]
- Added registry, hacked admin w/ new templates for category editor.
  [Justin Quick]
- Added ability to register fields to models. [Jose Soares]
- Added registry, hacked admin w/ new templates for category editor.
  [Justin Quick]
- Added an optional setting to allow the slug to be changed. [Corey
  Oordt]
- Added a new templatetag to retrieve the top level categories. [Jose
  Soares]
- Added views. [Jonathan Hensley]
- Added new documentation. [Corey Oordt]
- Added a description field. [Corey Oordt]
- Added some sample config to see it work. [Corey Oordt]
- Added a template for the template tags. [Corey Oordt]
- Added a demo file of music genres. [Corey Oordt]
- Added tests for templatetags. [Corey Oordt]
- Upped the version and separated the editor. [Corey Oordt]
- Added some testing fixtures. [Corey Oordt]
- Added some tests for category importing. [Corey Oordt]
- Started the docs. [Corey Oordt]
- Added a command to import categories from a file. [Corey Oordt]
- Added the editor templates. [Corey Oordt]
- Added to the gitignore. [Corey Oordt]
- Added template for category detail. [Jose Soares]
- Added urls and views for category detail. [Jose Soares]
- Getting the admin interface working. [Corey Oordt]

### Fix

- Fixed a typo in the setup.py and wrapped the other django import in
  __init__.py so you could call get_version without having django
  installed. Also increased the version number to 0.2.1. [Corey Oordt]
- Fixed the get_absolute_url for the Categories model and fixed up the
  view as well. [Corey Oordt]
- Fixing up and updating the usage. [Corey Oordt]
- Fixed up the readme to include some goals. [Corey Oordt]
- Tweaked the description and example of the template tag. [Corey Oordt]
- Fixed a wrong relative path with the jsi18n admin script. [Corey
  Oordt]

### Updates

- Modified the setup.py to get the latest version from the code and the
  long_description fro the README.txt file. [Corey Oordt]
- Altered the registration naming so more than one field could be
  registered for a model. [Corey Oordt]
- Changed the disclosure triangle to be a unicode character instead of
  the images. [Corey Oordt]
- Updated tree editor view. [jhensley]

### Other

- Tiered template heirarchy. [Justin Quick]
- Removed the special many2many models. The user interface was just too
  odd to implement. [Corey Oordt]
- Removed the permalink decorator to make the absoluteurl work. [Corey
  Oordt]
- Fixed most of the tests. [Corey Oordt]
- Moving media files around. [Corey Oordt]
- Split the editor into a separate app. [Corey Oordt]
