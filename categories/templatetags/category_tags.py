from django import template
from categories.models import Category
from mptt.utils import drilldown_tree_for_node

class CategoryNode(template.Node):
    
    def __init__(self, category, varname):
        if category.startswith('"') and category.endswith('"'):
            self.category = category[1:-1]
        else:
            self.category = category
        
        if self.category.startswith('/'):
            self.category = self.category[1:]
        else:
            self.category = category
        if self.category.endswith('/'):
            self.category = self.category[:-1]
        
        self.varname = varname
    
    def render(self, context):
        try:
            cat_list = self.category.split('/')
            categories = Category.objects.filter(name = cat_list[-1], level=len(cat_list)-1)
            
            if len(cat_list) == 1 and len(categories) > 1:
                context[self.varname] = None
                return ''
            if len(categories) == 1:
                context[self.varname] = drilldown_tree_for_node(categories[0])
            else:
                for item in categories:
                    if item.parent.name == cat_list[-2]:
                        context[self.varname] = drilldown_tree_for_node(item)
        except Category.DoesNotExist:
            context[self.varname] = None
        return ''


def get_category(parser, token):
    """
    Retrieves the specified category tree.
    
    Syntax::
    
        {% get_category "category name" as varname %}
        
    Example::
    
        {% get_category "/Rock" as rock %}
        {% get_category "/Rock/C-Rock" as crock %}    
    """
    bits = token.contents.split()
    error_str = '%(tagname)s tag should be in the format {%% %(tagname)s ' \
                '"category name" as varname %%}.'
    if len(bits) != 4 or bits[2] != 'as':
        raise template.TemplateSyntaxError, error_str % {'tagname': bits[0]}
    category = bits[1]
    varname = bits[3]
    return CategoryNode(category, varname)

register = template.Library()
register.tag(get_category)
