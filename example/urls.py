import os

from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve

admin.autodiscover()


ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

urlpatterns = (
    # Example:
    # (r'^sample/', include('sample.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^categories/', include('categories.urls')),
    # r'^cats/', include('categories.urls')),

    url(r'^static/categories/(?P<path>.*)$', serve,
        {'document_root': ROOT_PATH + '/categories/media/categories/'}),

    # (r'^static/editor/(?P<path>.*)$', 'django.views.static.serve',
    #     {'document_root': ROOT_PATH + '/editor/media/editor/',
    #      'show_indexes':True}),

    url(r'^static/(?P<path>.*)$', serve, {'document_root': os.path.join(ROOT_PATH, 'example', 'static')}),

)
