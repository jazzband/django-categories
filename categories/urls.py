from django.conf.urls import url
from django.views.generic import ListView
from .models import Category
from . import views


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
