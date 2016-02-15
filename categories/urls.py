from django.conf.urls import url
from .models import Category
from . import views

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

urlpatterns = (
    url(
        r'^$', ListView.as_view(**categorytree_dict), name='categories_tree_list'
    ),
)

urlpatterns += (
    url(r'^(?P<path>.+)/$', views.category_detail, name='categories_category'),
)
