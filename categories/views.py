from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from categories.models import Category
from django.views.decorators.cache import cache_page
from django.core.urlresolvers import reverse

def category_detail(request, path, with_stories=False, 
    template_name='categories/category_detail.html'):
    
    path_items = path.strip('/').split('/')
    slug = path_items[-1]
    level = len(path_items)
    context = {}
    category = get_object_or_404(Category,
        slug__iexact=slug, level=level-1)
        
    context['category'] = category
        
    return render_to_response(template_name,
        context,
        context_instance=RequestContext(request)
    )
