from django.conf.urls.defaults import *
from categories.models import *

categorytree_dict = {
    'queryset': CategoryTree.objects.all()
}

urlpatterns = patterns('django.views.generic.list_detail',
    url(
        r'^$', 'object_list', categorytree_dict, name='categories_tree_list'
    ),
    url(
        r'^(?P<slug>[\w-]+)/$', 'object_detail', categorytree_dict, name='categories_tree'
    ),
)

urlpatterns += patterns('categories.views',
    url(r'^(?P<slug>[\w-]+)/(?P<category_slug>[\w\-\/]+)/$', 'category_detail', name='categories_category'),
)