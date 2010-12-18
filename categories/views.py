from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
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