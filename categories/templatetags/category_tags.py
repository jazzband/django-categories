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
        self.category = template.Variable(category)
        self.varname = varname
    
    def render(self, context):
        try:
            category = self.category.resolve(context)
        except template.VariableDoesNotExist:
            category = self.category.var
        try:
            if category is not None:
                context[self.varname] = drilldown_tree_for_node(category)
            else:
                context[self.varname] = []
        except Category.DoesNotExist:
            context[self.varname] = []
        return ''

@register.tag
def get_category_drilldown(parser, token):
    """
    Retrieves the specified category, its ancestors and its immediate children
    as an iterable.
    
    Syntax::
    
        {% get_category_drilldown "category name" as varname %}
        
    Example::
    
        {% get_category_drilldown "/Grandparent/Parent" as family %}
    
    or ::
    
        {% get_category_drilldown category_obj as family %}
    
    Sets family to::
    
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

@register.inclusion_tag('categories/breadcrumbs.html')
def breadcrumbs(category,separator="/"):
    """
    Render breadcrumbs, using the ``categories/breadcrumbs.html`` template, 
    using the optional ``separator`` argument.
    """
    if isinstance(category, Category):
        cat = category
    else:
        cat = get_category(category)
    
    return {'category': cat, 'separator': separator}

@register.inclusion_tag('categories/ul_tree.html')
def display_drilldown_as_ul(category):
    """
    Render the category with ancestors, but no children using the 
    ``categories/ul_tree.html`` template.
    
    Example::
    
        {% display_drilldown_as_ul "/Grandparent/Parent" %}
    
    or ::
    
        {% display_drilldown_as_ul category_obj %}
    
    Returns::
    
        <ul>
          <li><a href="/categories/">Top</a>
          <ul>
            <li><a href="/categories/grandparent/">Grandparent</a>
            <ul>
              <li><a href="/categories/grandparent/parent/">Parent</a>
              <ul>
                <li><a href="/categories/grandparent/parent/child1">Child1</a></li>
                <li><a href="/categories/grandparent/parent/child2">Child2</a></li>
                <li><a href="/categories/grandparent/parent/child3">Child3</a></li>
              </ul>
              </li>
            </ul>
            </li>
          </ul>
          </li>
        </ul>
    """
    if isinstance(category, Category):
        cat = category
    else:
        cat = get_category(category)
    
    return {'category': cat, 'path': drilldown_tree_for_node(cat) or []}

@register.inclusion_tag('categories/ul_tree.html')
def display_path_as_ul(category):
    """
    Render the category with ancestors, but no children using the 
    ``categories/ul_tree.html`` template.
    
    Example::
    
        {% display_path_as_ul "/Grandparent/Parent" %}
    
    or ::
    
        {% display_path_as_ul category_obj %}
    
    Returns::
    
        <ul>
            <li><a href="/categories/">Top</a>
            <ul>
                <li><a href="/categories/grandparent/">Grandparent</a></li>
            </ul>
            </li>
        </ul>
    """
    if isinstance(category, Category):
        cat = category
    else:
        cat = get_category(category)
    
    return {'category': cat, 'path': cat.get_ancestors() or []}

class TopLevelCategoriesNode(template.Node):
    def __init__(self, varname):
        self.varname = varname
    
    def render(self, context):
        context[self.varname] = Category.objects.filter(parent=None).order_by('name')
        return ''

@register.tag
def get_top_level_categories(parser, token):
    """
    Retrieves an alphabetical list of all the categories with with no parents.
    
    Syntax::
    
        {% get_top_level_categories as categories %}
    
    Returns an list of categories [<category>, <category>, <category, ...]
    """
    bits = token.contents.split()
    if len(bits) != 3:
        raise template.TemplateSyntaxError(
            "Usage: {%% %s as <variable> %%}" % bits[0]
        )
    if bits[1] != 'as':
        raise template.TemplateSyntaxError(
            "Usage: {%% %s as <variable> %%}" % bits[0]
        )
    return TopLevelCategoriesNode(bits[2])
