import django
from django.db import models
from django.template import Library
from django.contrib.admin.templatetags.admin_list import result_headers, _boolean_icon
from django.contrib.admin.utils import lookup_field
from categories.editor.utils import display_for_field
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_text, force_text
from django.utils.html import escape, conditional_escape
from django.utils.safestring import mark_safe

from categories.editor import settings

register = Library()

TREE_LIST_RESULTS_TEMPLATE = 'admin/editor/tree_list_results.html'
if settings.IS_GRAPPELLI_INSTALLED:
    TREE_LIST_RESULTS_TEMPLATE = 'admin/editor/grappelli_tree_list_results.html'


def get_empty_value_display(cl):
    if hasattr(cl.model_admin, 'get_empty_value_display'):
        return cl.model_admin.get_empty_value_display()
    else:
        # Django < 1.9
        from django.contrib.admin.views.main import EMPTY_CHANGELIST_VALUE
        return EMPTY_CHANGELIST_VALUE


def items_for_tree_result(cl, result, form):
    """
    Generates the actual list of data.
    """
    first = True
    pk = cl.lookup_opts.pk.attname
    for field_name in cl.list_display:
        row_class = ''
        try:
            f, attr, value = lookup_field(field_name, result, cl.model_admin)
        except (AttributeError, ObjectDoesNotExist):
            result_repr = get_empty_value_display(cl)
        else:
            if f is None:
                if django.VERSION[1] == 4:
                    if field_name == 'action_checkbox':
                        row_class = ' class="action-checkbox disclosure"'
                allow_tags = getattr(attr, 'allow_tags', False)
                boolean = getattr(attr, 'boolean', False)
                if boolean:
                    allow_tags = True
                    result_repr = _boolean_icon(value)
                else:
                    result_repr = smart_text(value)
                # Strip HTML tags in the resulting text, except if the
                # function has an "allow_tags" attribute set to True.
                if not allow_tags:
                    result_repr = escape(result_repr)
                else:
                    result_repr = mark_safe(result_repr)
            else:
                if value is None:
                    result_repr = get_empty_value_display(cl)
                if isinstance(f.rel, models.ManyToOneRel):
                    result_repr = escape(getattr(result, f.name))
                else:
                    result_repr = display_for_field(value, f, '')
                if isinstance(f, models.DateField) or isinstance(f, models.TimeField):
                    row_class = ' class="nowrap"'
            if first:
                if django.VERSION[1] < 4:
                    try:
                        f, attr, checkbox_value = lookup_field('action_checkbox', result, cl.model_admin)
                        if row_class:
                            row_class = "%s%s" % (row_class[:-1], ' disclosure"')
                        else:
                            row_class = ' class="disclosure"'
                    except (AttributeError, ObjectDoesNotExist):
                        pass

        if force_text(result_repr) == '':
            result_repr = mark_safe('&nbsp;')
        # If list_display_links not defined, add the link tag to the first field
        if (first and not cl.list_display_links) or field_name in cl.list_display_links:
            if django.VERSION[1] < 4:
                table_tag = 'td'  # {True:'th', False:'td'}[first]
            else:
                table_tag = {True: 'th', False: 'td'}[first]

            url = cl.url_for_result(result)
            # Convert the pk to something that can be used in Javascript.
            # Problem cases are long ints (23L) and non-ASCII strings.
            if cl.to_field:
                attr = str(cl.to_field)
            else:
                attr = pk
            value = result.serializable_value(attr)
            result_id = repr(force_text(value))[1:]
            first = False
            if django.VERSION[1] < 4:
                yield mark_safe(
                    '<%s%s>%s<a href="%s"%s>%s</a></%s>' %
                    (table_tag, row_class, checkbox_value, url, (cl.is_popup and ' onclick="opener.dismissRelatedLookupPopup(window, %s); return false;"' % result_id or ''), conditional_escape(result_repr), table_tag))
            else:
                yield mark_safe(
                    '<%s%s><a href="%s"%s>%s</a></%s>' %
                    (table_tag, row_class, url, (cl.is_popup and ' onclick="opener.dismissRelatedLookupPopup(window, %s); return false;"' % result_id or ''), conditional_escape(result_repr), table_tag))

        else:
            # By default the fields come from ModelAdmin.list_editable, but if we pull
            # the fields out of the form instead of list_editable custom admins
            # can provide fields on a per request basis
            if form and field_name in form.fields:
                bf = form[field_name]
                result_repr = mark_safe(force_text(bf.errors) + force_text(bf))
            else:
                result_repr = conditional_escape(result_repr)
            yield mark_safe('<td%s>%s</td>' % (row_class, result_repr))
    if form and not form[cl.model._meta.pk.name].is_hidden:
        yield mark_safe('<td>%s</td>' % force_text(form[cl.model._meta.pk.name]))


class TreeList(list):
    pass


def tree_results(cl):
    if cl.formset:
        for res, form in zip(cl.result_list, cl.formset.forms):
            result = TreeList(items_for_tree_result(cl, res, form))
            if hasattr(res, 'pk'):
                result.pk = res.pk
                if res.parent:
                    result.parent_pk = res.parent.pk
                else:
                    res.parent_pk = None
            yield result
    else:
        for res in cl.result_list:
            result = TreeList(items_for_tree_result(cl, res, None))
            if hasattr(res, 'pk'):
                result.pk = res.pk
                if res.parent:
                    result.parent_pk = res.parent.pk
                else:
                    res.parent_pk = None
            yield result


def result_tree_list(cl):
    """
    Displays the headers and data list together
    """
    import django
    result = {
        'cl': cl,
        'result_headers': list(result_headers(cl)),
        'results': list(tree_results(cl))
    }
    if django.VERSION[1] > 2:
        from django.contrib.admin.templatetags.admin_list import result_hidden_fields
        result['result_hidden_fields'] = list(result_hidden_fields(cl))
    return result
result_tree_list = register.inclusion_tag(TREE_LIST_RESULTS_TEMPLATE)(result_tree_list)
