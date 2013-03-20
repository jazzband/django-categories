from django.conf.urls import patterns, url
from .models import Category

try:
    from django.views.generic import DetailView, ListView
except ImportError:
    try:
        from cbv import DetailView, ListView
    except ImportError:
        from django.core.exceptions import ImproperlyConfigured
        raise ImproperlyConfigured("For older versions of Django, you need django-cbv.")


categorytree_dict = {
    'queryset': Category.objects.filter(level=0)
}

urlpatterns = patterns('',
    url(
        r'^$', ListView.as_view(**categorytree_dict), name='categories_tree_list'
    ),
)

urlpatterns += patterns('categories.views',
    url(r'^(?P<path>.+)/$', 'category_detail', name='categories_category'),
)
