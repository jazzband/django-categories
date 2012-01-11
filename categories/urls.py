from django.conf.urls.defaults import *
from .models import Category

categorytree_dict = {
    'queryset': Category.objects.filter(level=0)
}

urlpatterns = patterns('django.views.generic.list_detail',
    url(
        r'^$', 'object_list', categorytree_dict, name='categories_tree_list'
    ),
)

urlpatterns += patterns('categories.views',
    url(r'^(?P<path>.+)/$', 'category_detail', name='categories_category'),
)