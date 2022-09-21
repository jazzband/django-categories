"""View functions for categories."""
from typing import Optional

from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import select_template
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView

from .models import Category


def category_detail(
    request, path, template_name="categories/category_detail.html", extra_context: Optional[dict] = None
):
    """Render the detail page for a category."""
    extra_context = extra_context or {}
    path_items = path.strip("/").split("/")
    if len(path_items) >= 2:
        category = get_object_or_404(
            Category, slug__iexact=path_items[-1], level=len(path_items) - 1, parent__slug__iexact=path_items[-2]
        )
    else:
        category = get_object_or_404(Category, slug__iexact=path_items[-1], level=len(path_items) - 1)

    templates = []
    while path_items:
        templates.append("categories/%s.html" % "_".join(path_items))
        path_items.pop()
    templates.append(template_name)

    context = {"category": category}
    if extra_context:
        context.update(extra_context)
    return HttpResponse(select_template(templates).render(context))


def get_category_for_path(path, queryset=Category.objects.all()):
    """Return the category for a path."""
    path_items = path.strip("/").split("/")
    if len(path_items) >= 2:
        queryset = queryset.filter(
            slug__iexact=path_items[-1], level=len(path_items) - 1, parent__slug__iexact=path_items[-2]
        )
    else:
        queryset = queryset.filter(slug__iexact=path_items[-1], level=len(path_items) - 1)
    return queryset.get()


class CategoryDetailView(DetailView):
    """Detail view for a category."""

    model = Category
    path_field = "path"

    def get_object(self, **kwargs):
        """Get the category."""
        if self.path_field not in self.kwargs:
            raise AttributeError(
                "Category detail view %s must be called with " "a %s." % (self.__class__.__name__, self.path_field)
            )
        if self.queryset is None:
            queryset = self.get_queryset()
        try:
            return get_category_for_path(self.kwargs[self.path_field], self.model.objects.all())
        except Category.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query") % {"verbose_name": queryset.model._meta.verbose_name}
            )

    def get_template_names(self):
        """Get the potential template names."""
        names = []
        path_items = self.kwargs[self.path_field].strip("/").split("/")
        while path_items:
            names.append("categories/%s.html" % "_".join(path_items))
            path_items.pop()
        names.extend(super(CategoryDetailView, self).get_template_names())
        return names


class CategoryRelatedDetail(DetailView):
    """Detailed view for a category relation."""

    path_field = "category_path"
    object_name_field = None

    def get_object(self, **kwargs):
        """Get the object to render."""
        if self.path_field not in self.kwargs:
            raise AttributeError(
                "Category detail view %s must be called with " "a %s." % (self.__class__.__name__, self.path_field)
            )
        queryset = super(CategoryRelatedDetail, self).get_queryset()
        try:
            category = get_category_for_path(self.kwargs[self.path_field])
        except Category.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query") % {"verbose_name": queryset.model._meta.verbose_name}
            )
        return queryset.get(category=category)

    def get_template_names(self):
        """Get all template names."""
        names = []
        opts = self.object._meta
        path_items = self.kwargs[self.path_field].strip("/").split("/")
        if self.object_name_field:
            path_items.append(getattr(self.object, self.object_name_field))
        while path_items:
            names.append(
                "%s/category_%s_%s%s.html"
                % (opts.app_label, "_".join(path_items), opts.object_name.lower(), self.template_name_suffix)
            )
            path_items.pop()
        names.append("%s/category_%s%s.html" % (opts.app_label, opts.object_name.lower(), self.template_name_suffix))
        names.extend(super(CategoryRelatedDetail, self).get_template_names())
        return names


class CategoryRelatedList(ListView):
    """List related category items."""

    path_field = "category_path"

    def get_queryset(self):
        """Get the list of items."""
        if self.path_field not in self.kwargs:
            raise AttributeError(
                "Category detail view %s must be called with " "a %s." % (self.__class__.__name__, self.path_field)
            )
        queryset = super(CategoryRelatedList, self).get_queryset()
        category = get_category_for_path(self.kwargs[self.path_field])
        return queryset.filter(category=category)

    def get_template_names(self):
        """Get the template names."""
        names = []
        if hasattr(self.object_list, "model"):
            opts = self.object_list.model._meta
            path_items = self.kwargs[self.path_field].strip("/").split("/")
            while path_items:
                names.append(
                    "%s/category_%s_%s%s.html"
                    % (opts.app_label, "_".join(path_items), opts.object_name.lower(), self.template_name_suffix)
                )
                path_items.pop()
            names.append(
                "%s/category_%s%s.html" % (opts.app_label, opts.object_name.lower(), self.template_name_suffix)
            )
        names.extend(super(CategoryRelatedList, self).get_template_names())
        return names
