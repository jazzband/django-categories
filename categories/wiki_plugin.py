# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.forms import modelform_factory
from django.conf.urls import include, url
from django.utils.translation import ugettext as _
from wiki.core.plugins import registry
from wiki.models import Article
from wiki.core.plugins.base import BasePlugin
from wiki.plugins.notifications.settings import ARTICLE_EDIT
from wiki.plugins.notifications.util import truncate_title
from . import views, settings, forms, models

class CategoryPlugin(BasePlugin):

    '''This class initializes the entirety of categories for the app, and also allows
     the editing and creation of new categories through the 'edit sidebar' and 'tab' respectively'''

    slug = 'categories'

    # for editing of which categories the article is in
    sidebar = {
        'headline': _('Change this article\'s Categories'),
        'icon_class': 'fa-sitemap',
        'template': 'sidebar.html',
        'form_class': forms.SidebarForm,
        'get_form_kwargs': (lambda a: {})
    }


    article_tab = (_('Categories'), "fa fa-sitemap")
    article_view = views.CategoryView.dispatch

    urlpatterns = { 'article': [
      url(r'^$', views.CategoryView.as_view(), name ='categories_list'),
    ]}

    def __init__(self):	
        # print "I WAS LOADED!"
        pass




class CategoryEditPlugin(BasePlugin):

    '''created this separate plugin to create a separate category edit sidebar plugin so that we can edit
     category parent if on a category landing article'''

    slug = 'categoryEdit'

    sidebar = {
        'headline': _('Edit this Category'),
        'icon_class': 'fa-sitemap',
        'template': 'sidebarEdit.html',
        'form_class': forms.EditCategoryForm,
        'get_form_kwargs': (lambda a: {})
    }


    def __init__(self):
        # print "I WAS LOADED!"
        pass


# register both plugins

registry.register(CategoryPlugin)
registry.register(CategoryEditPlugin)
