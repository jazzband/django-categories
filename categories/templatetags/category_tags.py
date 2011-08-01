from django import template
from django.template import Library, Node, TemplateSyntaxError, \
    Variable, resolve_variable, VariableDoesNotExist, Context
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
    Render the category with ancestors and children using the
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
    Retrieves an alphabetical list of all the categories that have no parents.

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

def resolve(var, context):
    try:
        return var.resolve(context)
    except VariableDoesNotExist:
        try:
            return var.var
        except AttributeError:
            return var

def get_latest_objects_by_category(category, app_label, model_name, set_name, 
                                    date_field='pub_date', num=15):
    m = get_model(app_label, model_name)
    if not isinstance(category, Category):
        category = Category.objects.get(slug=str(category))
    children = Category.objects.filter(parent=category)
    ids = []
    for cat in list(children) + [category]:
        if hasattr(cat, '%s_set' % set_name):
            ids.extend([x.pk for x in getattr(cat, '%s_set' % set_name).all()[:num]])
    
    return m.objects.filter(pk__in=ids).order_by('-%s' % date_field)[:num]

class LatestObjectsNode(Node):
    def __init__(self, var_name, category, app_label, model_name, set_name, 
                 date_field='pub_date', num=15):
        """Get latest objects of app_label.model_name"""
        self.category = Variable(category)
        self.app_label = Variable(app_label)
        self.model_name = Variable(model_name)
        self.set_name = Variable(set_name)
        self.date_field = Variable(date_field)
        self.num = Variable(num)
        self.var_name = var_name
    
    def get_cache_key(self, category, app_label, model_name, set_name, 
                     date_field, num):
        """Get the cache key"""
        key = 'latest_objects.%s' % '.'.join([category, app_label, model_name, 
                set_name, date_field, num])
    
    def render(self, context):
        """Render this sucker"""
        category = resolve(self.category, context)
        app_label = resolve(self.app_label, context)
        model_name = resolve(self.model_name, context)
        set_name = resolve(self.set_name, context)
        date_field = resolve(self.date_field, context)
        num = resolve(self.num, context)
        
        cache_key = self.get_cache_key(category, app_label, model_name, set_name, 
                         date_field, num)
        result = cache.get(cache_key)
        if not result:
            result = get_latest_objects_by_category(category, app_label, model_name, 
                            set_name, date_field, num)
        
            cache.set(key, result, 300)
        context[self.var_name] = result
        
        return ''

def do_get_latest_objects_by_category(parser, token):
    """
    Get the latest objects by category
    
    {% get_latest_objects_by_category category app_name model_name set_name [date_field] [number] as [var_name] %}
    """
    proper_form = "{% get_latest_objects_by_category category app_name model_name set_name [date_field] [number] as [var_name] %}"
    bits = token.split_contents()
    
    if bits[-2] != 'as':
        raise TemplateSyntaxError("%s tag shoud be in the form: %s" % (bits[0], proper_form))
    if len(bits) < 7:
        raise TemplateSyntaxError("%s tag shoud be in the form: %s" % (bits[0], proper_form))
    if len(bits) > 9:
        raise TemplateSyntaxError("%s tag shoud be in the form: %s" % (bits[0], proper_form))
    category = bits[1]
    app_label = bits[2]
    model_name = bits[3]
    set_name = bits[4]
    var_name = bits[-1]
    if bits[5] != 'as':
        date_field = bits[5]
    else:
        date_field = None
    if bits[6] != 'as':
        num = bits[6]
    else:
        num = None
    return LatestObjectsNode(var_name, category, app_label, model_name, set_name, 
                     date_field, num)