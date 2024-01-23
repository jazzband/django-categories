# Django Categories

[![Jazzband](https://jazzband.co/static/img/badge.svg)](https://jazzband.co/)
[![codecov](https://codecov.io/gh/jazzband/django-categories/branch/master/graph/badge.svg?token=rW8mpdZqWQ)](https://codecov.io/gh/jazzband/django-categories)

Django Categories grew out of our need to provide a basic hierarchical taxonomy management system that multiple applications could use independently or in concert.

As a news site, our stories, photos, and other content get divided into "sections" and we wanted all the apps to use the same set of sections. As our needs grew, the Django Categories grew in the functionality it gave to category handling within web pages.

## Features of the project

**Multiple trees, or a single tree.**
You can treat all the records as a single tree, shared by all the applications. You can also treat each of the top level records as individual trees, for different apps or uses.

**Easy handling of hierarchical data.**
We use [Django MPTT](http://pypi.python.org/pypi/django-mptt) to manage the data efficiently and provide the extra access functions.

**Easy importation of data.**
Import a tree or trees of space- or tab-indented data with a Django management command.

**Metadata for better SEO on web pages**
Include all the metadata you want for easy inclusion on web pages.

**Link uncategorized objects to a category**
Attach any number of objects to a category, even if the objects themselves aren't categorized.

**Hierarchical Admin**
Shows the data in typical tree form with disclosure triangles

**Template Helpers**
Easy ways for displaying the tree data in templates:

- **Show one level of a tree.** All root categories or just children of a specified category

- **Show multiple levels.** Ancestors of category, category and all children of category or  a category and its children

## Categories API

Support for categories API can be added by third party application [django-categories-api](https://github.com/PetrDlouhy/django-categories-api).

**Optional Thumbnail field.**
Have a thumbnail for each category!

**"Categorize" models in settings.**
Now you don't have to modify the model to add a `Category` relationship. Use the new settings to "wire" categories to different models.
