from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


import os

ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

urlpatterns = patterns('',
    # Example:
    # (r'^sample/', include('sample.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^categories/', include('categories.urls')),
    #(r'^cats/', include('categories.urls')),

    (r'^static/categories/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': ROOT_PATH + '/categories/media/categories/'}),

    (r'^static/editor/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': ROOT_PATH + '/editor/media/editor/',
         'show_indexes':True}),
)