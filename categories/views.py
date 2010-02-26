from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.template.loader import select_template
from categories.models import Category

@cache_page(3600)
def category_detail(request, path, with_stories=False, 
    template_name='categories/category_detail.html'):
    path_items = path.strip('/').split('/')
    category = get_object_or_404(Category,
            slug__iexact = path_items[-1],
            level = len(path_items)-1)
    template = select_template((
        'categories/%s.html' % '_'.join(path_items),
        template_name,
    ))
    context = RequestContext(request)
    context.update({'category':category})
    return HttpResponse(template.render(context))