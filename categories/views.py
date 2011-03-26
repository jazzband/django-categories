from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, Http404
from django.views.decorators.cache import cache_page
from django.template.loader import select_template
from categories.models import Category
from settings import CACHE_VIEW_LENGTH

@cache_page(CACHE_VIEW_LENGTH)
def category_detail(request, path, 
    template_name='categories/category_detail.html', extra_context={}):
    path_items = path.strip('/').split('/')
    if len(path_items) >= 2:
        category = get_object_or_404(Category,
            slug__iexact = path_items[-1],
            level = len(path_items)-1,
            parent__slug__iexact=path_items[-2])
    else:
        category = get_object_or_404(Category,
            slug__iexact = path_items[-1],
            level = len(path_items)-1)
    
    templates = []
    while path_items:
        templates.append('categories/%s.html' % '_'.join(path_items))
        path_items.pop()
    templates.append(template_name)

    context = RequestContext(request)
    context.update({'category':category})
    if extra_context:
        context.update(extra_context)
    return HttpResponse(select_template(templates).render(context))


import django
if django.VERSION[0] >= 1 and django.VERSION[1] >= 3:
    from django.views.generic import DetailView

    class CategoryDetailView(DetailView):

        model = Category
        path_field = 'path'

        def get_object(self, **kwargs):
            if self.path_field not in self.kwargs:
                raise AttributeError(u"Category detail view %s must be called with "
                                     u"a %s." % self.__class__.__name__, self.path_field)
            if self.queryset is None:
                 queryset = self.get_queryset()

            self.path_items = self.kwargs[self.path_field].strip('/').split('/')
            if len(self.path_items) >= 2:
                queryset = queryset.filter(
                    slug__iexact = self.path_items[-1],
                    level = len(self.path_items)-1,
                    parent__slug__iexact=self.path_items[-2])
            else:
                queryset = queryset.filter(
                    slug__iexact = self.path_items[-1],
                    level = len(self.path_items)-1)

            try:
                obj = queryset.get()
            except ObjectDoesNotExist:
                raise Http404(_(u"No %(verbose_name)s found matching the query") %
                              {'verbose_name': queryset.model._meta.verbose_name})
            return obj
        
        def get_template_names(self):
            names = []
            path_items = self.path_items
            while path_items:
                names.append('categories/%s.html' % '_'.join(path_items))
                path_items.pop()
            names.extend(super(CategoryDetailView, self).get_template_names())
            return names