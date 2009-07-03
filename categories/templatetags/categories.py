from django import template
from ellington.categories.models import Category

class CategoryNode(template.Node):
    def __init__(self, category, varname, hierarchy):
        # TODO: improve quote removal. ``[1:-1]`` feels icky.
        if '\"' in category:
            self.category = category[1:-1]
        else:
            self.category = category
        self.varname = varname
        if '\"' in hierarchy:
            self.hierarchy = hierarchy[1:-1]
        else:
            self.hierarchy = hierarchy

    def render(self, context):
        try:
            context[self.varname] = Category.objects.get(
                hierarchy__slug=self.hierarchy,
                slug_path=self.category)
        except Category.DoesNotExist:
            context[self.varname] = None
        return ''

def get_category(parser, token):
    """
    Retrieves the specified category.

    Syntax::

        {% get_category [category] as varname [hierarchy slug] %}

    Example::

        {% get_category "/agriculture/dairy" as dairy hierarchy "business" %}

    [hierarchy slug] is optional. If not specified, the "news" hierarchy
    will be used.
    """
    bits = token.contents.split()
    if len(bits) < 4:
        raise template.TemplateSyntaxError, "%s tag requires at least three arguments." % bits[0]
    if bits[2] != 'as':
        raise template.TemplateSyntaxError, "%s tag requires the third argument to be 'as'." % bits[0]
    if not len(bits) in (4, 6):
        raise template.TemplateSyntaxError, "%s tag requires exactly 3, or 5 arguments." % bits[0]
    category = bits[1]
    varname = bits[3]
    hierarchy = "news"
    if len(bits) == 4:
        return CategoryNode(category, varname, hierarchy)
    elif len(bits) == 6:
        if bits[4] == 'hierarchy':
            return CategoryNode(category, varname, bits[5])
        else:
            raise template.TemplateSyntaxError, "Fifth argument to %s tag must be 'hierarchy'" % bits[0]
    else:
        raise template.TemplateSyntaxError, "Arguments to %s tag are malformed." % bits[0]

register = template.Library()
register.tag(get_category)
