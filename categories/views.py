import django
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from django.http import HttpResponse, Http404
from django.views.decorators.cache import cache_page
from django.template.loader import select_template
from django.utils.translation import ugettext as _

from .models import Category
from .settings import CACHE_VIEW_LENGTH

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


def get_category_for_path(path, queryset=Category.objects.all()):
    path_items = path.strip('/').split('/')
    if len(path_items) >= 2:
        queryset = queryset.filter(
            slug__iexact = path_items[-1],
            level = len(path_items)-1,
            parent__slug__iexact=path_items[-2])
    else:
        queryset = queryset.filter(
            slug__iexact = path_items[-1],
            level = len(path_items)-1)
    return queryset.get()

try:
    import cbv
    HAS_CBV = True
except ImportError:
    HAS_CBV = False

if ((django.VERSION[0] >= 1 and django.VERSION[1] >= 3) or HAS_CBV):
    if HAS_CBV:
        from cbv import DetailView, ListView
    else:
        from django.views.generic import DetailView, ListView

    class CategoryDetailView(DetailView):

        model = Category
        path_field = 'path'

        def get_object(self, **kwargs):
            if self.path_field not in self.kwargs:
                raise AttributeError(u"Category detail view %s must be called with "
                                     u"a %s." % self.__class__.__name__, self.path_field)
            if self.queryset is None:
                 queryset = self.get_queryset()
            try:
                return get_category_for_path(self.kwargs[self.path_field])
            except ObjectDoesNotExist:
                raise Http404(_(u"No %(verbose_name)s found matching the query") %
                              {'verbose_name': queryset.model._meta.verbose_name})
        
        def get_template_names(self):
            names = []
            path_items = self.kwargs[self.path_field].strip('/').split('/')
            while path_items:
                names.append('categories/%s.html' % '_'.join(path_items))
                path_items.pop()
            names.extend(super(CategoryDetailView, self).get_template_names())
            return names


    class CategoryRelatedDetail(DetailView):
        
        path_field = 'category_path'
        object_name_field = None
        
        def get_object(self, **kwargs):
            queryset = super(CategoryRelatedDetail, self).get_queryset()
            category = get_category_for_path(self.kwargs[self.path_field])
            return queryset.get(category=category,slug=self.kwargs[self.slug_field])

        def get_template_names(self):
            names = []
            opts = self.object._meta
            path_items = self.kwargs[self.path_field].strip('/').split('/')
            if self.object_name_field:
                path_items.append(getattr(self.object, self.object_name_field))
            while path_items:
                names.append( '%s/category_%s_%s%s.html' % (opts.app_label,
                                                            '_'.join(path_items),
                                                            opts.object_name.lower(),
                                                            self.template_name_suffix)
                                                            )
                path_items.pop()
            names.append('%s/category_%s%s.html' % (opts.app_label, 
                                                    opts.object_name.lower(),
                                                    self.template_name_suffix)
                                                    )
            names.extend(super(CategoryRelatedDetail, self).get_template_names())
            return names


    class CategoryRelatedList(ListView):
        
        path_field = 'category_path'

        def get_queryset(self):
            queryset = super(CategoryRelatedList, self).get_queryset()
            category = get_category_for_path(self.kwargs['category_path'])
            return queryset.filter(category=category)

        def get_template_names(self):
            names = []
            if hasattr(self.object_list, 'model'):
                opts = self.object_list.model._meta
                path_items = self.kwargs[self.path_field].strip('/').split('/')
                while path_items:
                    names.append( '%s/category_%s_%s%s.html' % (opts.app_label,
                                                                '_'.join(path_items),
                                                                opts.object_name.lower(),
                                                                self.template_name_suffix)
                                                                )
                    path_items.pop()
                names.append('%s/category_%s%s.html' % (opts.app_label,
                                                        opts.object_name.lower(),
                                                        self.template_name_suffix)
                                                        )
            names.extend(super(CategoryRelatedList, self).get_template_names())
            return names