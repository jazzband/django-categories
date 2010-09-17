from django import template
from categories.models import Category
from mptt.utils import drilldown_tree_for_node
from mptt.templatetags.mptt_tags import tree_path, tree_info

register = template.Library()

register.filter("category_path", tree_path)
register.filter(tree_info)

def get_category(category_string):
    """
    Convert a string, including a path, and return the Category object
    """
    if category_string.startswith('"') and category_string.endswith('"'):
        category = category_string[1:-1]
    else:
        category = category_string
    
    if category.startswith('/'):
        category = category[1:]
    if category.endswith('/'):
        category = category[:-1]
    
    cat_list = category.split('/')
    if len(cat_list) == 0:
        return None
    try:
        categories = Category.objects.filter(name = cat_list[-1], level=len(cat_list)-1)
        if len(cat_list) == 1 and len(categories) > 1:
            return None
        # If there is only one, use it. If there is more than one, check 
        # if the parent matches the parent passed in the string
        if len(categories) == 1:
            return categories[0]
        else:
            for item in categories:
                if item.parent.name == cat_list[-2]:
                    return item
    except Category.DoesNotExist:
        return None


class CategoryDrillDownNode(template.Node):
    
    def __init__(self, category, varname):
        self.category = get_category(category)
        self.varname = varname
    
    def render(self, context):
        try:
            if self.category is not None:
                context[self.varname] = drilldown_tree_for_node(self.category)
            else:
                context[self.varname] = None
        except Category.DoesNotExist:
            context[self.varname] = None
        return ''


def get_category_drilldown(parser, token):
    """
    Retrieves the specified category, it's ancestors and its children as an iterable list.
    
    Syntax::
    
        {% get_category "category name" as varname %}
        
    Example::
    
        {% get_category "/Grandparent/Parent" as family %}
    
    Returns an iterable with::
    
        Grandparent, Parent, Child 1, Child 2, Child n
    
    """
    bits = token.contents.split()
    error_str = '%(tagname)s tag should be in the format {%% %(tagname)s ' \
                '"category name" as varname %%}.'
    if len(bits) != 4 or bits[2] != 'as':
        raise template.TemplateSyntaxError, error_str % {'tagname': bits[0]}
    category = bits[1]
    varname = bits[3]
    return CategoryDrillDownNode(category, varname)

register.tag(get_category_drilldown)

@register.inclusion_tag('categories/ancestors_ul.html')
def display_path_as_ul(category):
    """
    Display the category with ancestors, but no children.
    
    Example::
    
        {% display_path_as_ul "/Grandparent/Parent" %}
    
    Returns::
    
        <ul><li>Grandparent<ul><li>Parent</li></ul></li></ul>
    """
    cat = get_category(category)
    
    return {}
    
    
class TopLevelCategoriesNode(template.Node):
    def __init__(self, varname):
        self.varname = varname
        
    def render(self, context):
        context[self.varname] = Category.objects.filter(parent=None).order_by('name')
        return ''
        

def get_top_level_categories(parser, token):
    """
    Retrives an alphabetical list of all the categories with with no parents.
    
    Syntax::
    
        {% get_top_level_categories as categories %}
        
    Returns an list of categories
    
    """
    bits = token.contents.split()
    if len(bits) != 3:
        raise template.TemplateSyntaxError, "Tag %s must have 2 arguments." % bits[0]
    if bits[1] != 'as':
        raise template.TemplateSyntaxError, "First argyment must be 'as'."
    return TopLevelCategoriesNode(bits[2])
    
register.tag(get_top_level_categories)
