"""Template tags for categories."""
from typing import Any, Type, Union

from django import template
from django.apps import apps
from django.template import Node, TemplateSyntaxError, VariableDoesNotExist
from django.template.base import FilterExpression
from mptt.templatetags.mptt_tags import (
    RecurseTreeNode,
    full_tree_for_model,
    tree_info,
    tree_path,
)
from mptt.utils import drilldown_tree_for_node

from categories.base import CategoryBase
from categories.models import Category

register = template.Library()

register.filter("category_path", tree_path)
register.filter(tree_info)
register.tag("full_tree_for_category", full_tree_for_model)


def resolve(var: Any, context: dict) -> Any:
    """Aggressively resolve a variable."""
    try:
        return var.resolve(context)
    except VariableDoesNotExist:
        try:
            return var.var
        except AttributeError:
            return var


def get_cat_model(model):
    """
    Return a class from a string or class.
    """
    model_class = None
    try:
        if isinstance(model, str):
            model_class = apps.get_model(*model.split("."))
        elif issubclass(model, CategoryBase):
            model_class = model
        if model_class is None:
            raise TypeError
    except TypeError:
        raise TemplateSyntaxError("Unknown model submitted: %s" % model)
    return model_class


def get_category(category_string, model: Union[str, Type] = Category) -> Any:
    """
    Convert a string, including a path, and return the Category object.

    Args:
        category_string: The name or path of the category
        model: The name of or Category model to search in

    Returns:
        The found category object or None if no category was found
    """
    model_class = get_cat_model(model)
    category = str(category_string).strip("'\"")
    category = category.strip("/")

    cat_list = category.split("/")
    if len(cat_list) == 0:
        return None
    try:
        categories = model_class.objects.filter(name=cat_list[-1], level=len(cat_list) - 1)
        if len(cat_list) == 1 and len(categories) > 1:
            return None
        # If there is only one, use it. If there is more than one, check
        # if the parent matches the parent passed in the string
        if len(categories) == 1:
            return categories[0]

        for item in categories:
            if item.parent.name == cat_list[-2]:
                return item
    except model_class.DoesNotExist:
        return None


class CategoryDrillDownNode(template.Node):
    """A category drill down template node."""

    def __init__(self, category, varname, model):
        self.category = category
        self.varname = varname
        self.model = model

    def render(self, context):
        """Render this node."""
        category = resolve(self.category, context)
        if isinstance(category, CategoryBase):
            cat = category
        else:
            cat = get_category(category, self.model)
        try:
            context[self.varname] = drilldown_tree_for_node(cat) if cat is not None else []
        except Exception:
            context[self.varname] = []
        return ""


@register.tag
def get_category_drilldown(parser, token):
    """
    Retrieves the specified category, its ancestors and its immediate children as an Iterable.

    The basic syntax::

        {% get_category_drilldown "category name" [using "app.Model"] as varname %}

    Example:
        Using a string for the category name::

            {% get_category_drilldown "/Grandparent/Parent" as family %}

        or using a variable for the category::

            {% get_category_drilldown category_obj as family %}

        Sets family to::

            Grandparent, Parent, Child 1, Child 2, Child n

    Args:
        parser: The Django template parser.
        token: The tag contents

    Returns:
        The recursive tree node.

    Raises:
        TemplateSyntaxError: If the tag is malformed.
    """
    bits = token.split_contents()
    error_str = (
        "%(tagname)s tag should be in the format {%% %(tagname)s "
        '"category name" [using "app.Model"] as varname %%} or '
        "{%% %(tagname)s category_obj as varname %%}."
    )
    varname = model = ""
    if len(bits) == 4:
        if bits[2] != "as":
            raise template.TemplateSyntaxError(error_str % {"tagname": bits[0]})
        if bits[2] == "as":
            varname = bits[3].strip("'\"")
            model = "categories.category"
    elif len(bits) == 6:
        if bits[2] not in ("using", "as") or bits[4] not in ("using", "as"):
            raise template.TemplateSyntaxError(error_str % {"tagname": bits[0]})
        if bits[2] == "as":
            varname = bits[3].strip("'\"")
            model = bits[5].strip("'\"")
        if bits[2] == "using":
            varname = bits[5].strip("'\"")
            model = bits[3].strip("'\"")
    else:
        raise template.TemplateSyntaxError(error_str % {"tagname": bits[0]})
    category = FilterExpression(bits[1], parser)
    return CategoryDrillDownNode(category, varname, model)


@register.inclusion_tag("categories/breadcrumbs.html")
def breadcrumbs(category_string, separator=" > ", using="categories.category"):
    """
    Render breadcrumbs, using the ``categories/breadcrumbs.html`` template.

    The basic syntax::

        {% breadcrumbs "category" [separator=" > "] [using="categories.category"] %}

    Args:
        category_string: A variable reference to or the name of the category to display
        separator: The string to separate the categories
        using: A variable reference to or the name of the category model to search for.

    Returns:
        The inclusion template
    """
    cat = get_category(category_string, using)

    return {"category": cat, "separator": separator}


@register.inclusion_tag("categories/ul_tree.html")
def display_drilldown_as_ul(category, using="categories.Category"):
    """
    Render the category with ancestors and children using the ``categories/ul_tree.html`` template.

    Example:
        The template code of::

            {% display_drilldown_as_ul "/Grandparent/Parent" %}

        or::

            {% display_drilldown_as_ul category_obj %}

        might render as::

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

    Args:
        category: A variable reference to or the name of the category to display
        using: A variable reference to or the name of the category model to search for.

    Returns:
        The inclusion template
    """
    cat = get_category(category, using)
    if cat is None:
        return {"category": cat, "path": []}
    else:
        return {"category": cat, "path": drilldown_tree_for_node(cat)}


@register.inclusion_tag("categories/ul_tree.html")
def display_path_as_ul(category, using="categories.Category"):
    """
    Render the category with ancestors, but no children using the ``categories/ul_tree.html`` template.

    Examples:
        The template code of::

            {% display_path_as_ul "/Grandparent/Parent" %}

        or::

            {% display_path_as_ul category_obj %}

        might render as::

            <ul>
                <li><a href="/categories/">Top</a>
                <ul>
                    <li><a href="/categories/grandparent/">Grandparent</a></li>
                </ul>
                </li>
            </ul>

    Args:
        category: A variable reference to or the name of the category to display
        using: A variable reference to or the name of the category model to search for.

    Returns:
        The inclusion template
    """
    if isinstance(category, CategoryBase):
        cat = category
    else:
        cat = get_category(category, using)

    return {"category": cat, "path": cat.get_ancestors() or []}


class TopLevelCategoriesNode(template.Node):
    """Template node for the top level categories."""

    def __init__(self, varname, model):
        self.varname = varname
        self.model = model

    def render(self, context):
        """Render this node."""
        model = get_cat_model(self.model)
        context[self.varname] = model.objects.filter(parent=None).order_by("name")
        return ""


@register.tag
def get_top_level_categories(parser, token):
    """
    Retrieves an alphabetical list of all the categories that have no parents.

    The basic syntax is::

        {% get_top_level_categories [using "app.Model"] as categories %}

    Args:
        parser: The Django template parser.
        token: The tag contents

    Returns:
         Returns a list of categories [<category>, <category>, <category, ...]

    Raises:
        TemplateSyntaxError: If a queryset isn't provided
    """
    bits = token.split_contents()
    usage = 'Usage: {%% %s [using "app.Model"] as <variable> %%}' % bits[0]

    if len(bits) == 3:
        if bits[1] != "as":
            raise template.TemplateSyntaxError(usage)
        varname = bits[2]
        model = "categories.category"
    elif len(bits) == 5:
        if bits[1] not in ("as", "using") and bits[3] not in ("as", "using"):
            raise template.TemplateSyntaxError(usage)
        if bits[1] == "using":
            model = bits[2].strip("'\"")
            varname = bits[4].strip("'\"")
        else:
            model = bits[4].strip("'\"")
            varname = bits[2].strip("'\"")
    else:
        raise template.TemplateSyntaxError(usage)

    return TopLevelCategoriesNode(varname, model)


def get_latest_objects_by_category(category, app_label, model_name, set_name, date_field="pub_date", num=15):
    """Return a queryset of the latest objects of ``app_label.model_name`` in given category."""
    m = apps.get_model(app_label, model_name)
    if not isinstance(category, CategoryBase):
        category = Category.objects.get(slug=str(category))
    children = category.children.all()
    ids = []
    for cat in list(children) + [category]:
        if hasattr(cat, "%s_set" % set_name):
            ids.extend([x.pk for x in getattr(cat, "%s_set" % set_name).all()[:num]])

    return m.objects.filter(pk__in=ids).order_by("-%s" % date_field)[:num]


class LatestObjectsNode(Node):
    """
    Get latest objects of app_label.model_name.
    """

    def __init__(self, var_name, category, app_label, model_name, set_name, date_field="pub_date", num=15):
        self.category = category
        self.app_label = app_label
        self.model_name = model_name
        self.set_name = set_name
        self.date_field = date_field
        self.num = num
        self.var_name = var_name

    def render(self, context):
        """
        Render this sucker.
        """
        category = resolve(self.category, context)
        app_label = resolve(self.app_label, context)
        model_name = resolve(self.model_name, context)
        set_name = resolve(self.set_name, context)
        date_field = resolve(self.date_field, context)
        num = resolve(self.num, context)

        result = get_latest_objects_by_category(category, app_label, model_name, set_name, date_field, num)
        context[self.var_name] = result

        return ""


def do_get_latest_objects_by_category(parser, token):
    """
    Get the latest objects by category.

    The basic syntax is::

        {% get_latest_objects_by_category category app_name model_name set_name [date_field] [number] as [var_name] %}


    Args:
        parser: The Django template parser.
        token: The tag contents

    Returns:
        The latet objects node.

    Raises:
        TemplateSyntaxError: If the tag is malformed
    """
    proper_form = (
        "{% get_latest_objects_by_category category app_name model_name set_name "
        "[date_field] [number] as [var_name] %}"
    )
    bits = token.split_contents()

    if bits[-2] != "as":
        raise TemplateSyntaxError("%s tag shoud be in the form: %s" % (bits[0], proper_form))
    if len(bits) < 7:
        raise TemplateSyntaxError("%s tag shoud be in the form: %s" % (bits[0], proper_form))
    if len(bits) > 9:
        raise TemplateSyntaxError("%s tag shoud be in the form: %s" % (bits[0], proper_form))
    category = FilterExpression(bits[1], parser)
    app_label = FilterExpression(bits[2], parser)
    model_name = FilterExpression(bits[3], parser)
    set_name = FilterExpression(bits[4], parser)
    var_name = bits[-1]
    if bits[5] != "as":
        date_field = FilterExpression(bits[5], parser)
    else:
        date_field = FilterExpression(None, parser)
    if bits[6] != "as":
        num = FilterExpression(bits[6], parser)
    else:
        num = FilterExpression(None, parser)
    return LatestObjectsNode(var_name, category, app_label, model_name, set_name, date_field, num)


register.tag("get_latest_objects_by_category", do_get_latest_objects_by_category)


@register.filter
def tree_queryset(value):
    """
    Converts a normal queryset from an MPTT model to include all the ancestors.

    Allows a filtered subset of items to be formatted correctly

    Args:
        value: The queryset to convert

    Returns:
        The converted queryset
    """
    from copy import deepcopy

    from django.db.models.query import QuerySet

    if not isinstance(value, QuerySet):
        return value

    qs = value
    qs2 = deepcopy(qs)
    # Reaching into the bowels of query sets to find out whether the qs is
    # actually filtered and we need to do the INCLUDE_ANCESTORS dance at all.
    # INCLUDE_ANCESTORS is quite expensive, so don't do it if not needed.
    is_filtered = bool(qs.query.where.children)
    if is_filtered:
        include_pages = set()
        # Order by 'rght' will return the tree deepest nodes first;
        # this cuts down the number of queries considerably since all ancestors
        # will already be in include_pages when they are checked, thus not
        # trigger additional queries.
        for p in qs2.order_by("rght").iterator():
            if p.parent_id and p.parent_id not in include_pages and p.id not in include_pages:
                ancestor_id_list = p.get_ancestors().values_list("id", flat=True)
                include_pages.update(ancestor_id_list)

        if include_pages:
            qs = qs | qs.model._default_manager.filter(id__in=include_pages)

        qs = qs.distinct()
    return qs


@register.tag
def recursetree(parser, token):
    """
    Iterates over the nodes in the tree, and renders the contained block for each node.

    This tag will recursively render children into the template variable {{ children }}.
    Only one database query is required (children are cached for the whole tree)

    Example:
        Basic usage example::

            <ul>
                {% recursetree nodes %}
                    <li>
                        {{ node.name }}
                        {% if not node.is_leaf_node %}
                            <ul>
                                {{ children }}
                            </ul>
                        {% endif %}
                    </li>
                {% endrecursetree %}
            </ul>

    Args:
        parser: The Django template parser.
        token: The tag contents

    Returns:
        The recursive tree node.

    Raises:
        TemplateSyntaxError: If a queryset isn't provided.
    """
    bits = token.contents.split()
    if len(bits) != 2:
        raise template.TemplateSyntaxError("%s tag requires a queryset" % bits[0])
    queryset_var = FilterExpression(bits[1], parser)

    template_nodes = parser.parse(("endrecursetree",))
    parser.delete_first_token()

    return RecurseTreeNode(template_nodes, queryset_var)
