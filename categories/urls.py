"""URL patterns for the categories app."""
from django.urls import path, re_path
from django.views.generic import ListView

from . import views
from .models import Category

categorytree_dict = {"queryset": Category.objects.filter(level=0)}

urlpatterns = (path("", ListView.as_view(**categorytree_dict), name="categories_tree_list"),)

urlpatterns += (re_path(r"^(?P<path>.+)/$", views.category_detail, name="categories_category"),)
