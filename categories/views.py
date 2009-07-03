from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from ellington.categories.models import *

def category_detail(request, slug, category_slug):
    """
    A detail view of a category.

    Templates:
        :template:`categories/category_detail.html`
    Context:
        category
            A :model:`categories.Category` object.
    """
    category = get_object_or_404(Category,
        hierarchy__slug=slug,
        slug_path="/%s" % category_slug)
    return render_to_response('categories/category_detail.html',
        {'category' : category},
        context_instance=RequestContext(request)
    )
