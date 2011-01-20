from django.conf import settings as django_settings
from django.contrib import admin
from django.contrib.admin.util import unquote
from django.contrib.admin.views.main import ChangeList
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.utils import simplejson
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

import settings

class TreeChangeList(ChangeList):
    def get_ordering(self):
        if isinstance(self.model_admin, TreeEditor):
            return '', ''
        return super(ChangeList, self).get_ordering()

def _build_tree_structure(cls):
    """
    Build an in-memory representation of the item tree, trying to keep
    database accesses down to a minimum. The returned dictionary looks like
    this (as json dump):

        {"6": {"id": 6, "children": [7, 8, 10], "parent": null, "descendants": [7, 12, 13, 8, 10]},
         "7": {"id": 7, "children": [12], "parent": 6, "descendants": [12, 13]},
         "8": {"id": 8, "children": [], "parent": 6, "descendants": []},
         ...

    """
    all_nodes = { }
    def add_as_descendant(n, p):
        if not n: return
        all_nodes[n.id]['descendants'].append(p.id)
        add_as_descendant(n.parent, p)

    for p in cls.objects.order_by('tree_id', 'lft'):
        all_nodes[p.id] = { 'id': p.id, 'children' : [ ], 'descendants' : [ ], 'parent' : p.parent_id }
        if(p.parent_id):
            all_nodes[p.parent_id]['children'].append(p.id)
            add_as_descendant(p.parent, p)

    return all_nodes

class TreeEditor(admin.ModelAdmin):
    list_per_page = 10000 # We can't have pagination
    class Media:
        css = {'all':(settings.MEDIA_PATH + "jquery.treeTable.css",)}
        js = []

        js.extend((settings.MEDIA_PATH + "jquery.treeTable.js",))

    def __init__(self, *args, **kwargs):
        super(TreeEditor, self).__init__(*args, **kwargs)

        self.list_display = list(self.list_display)
        
        if 'action_checkbox' in self.list_display:
            self.list_display.remove('action_checkbox')

        opts = self.model._meta
        self.change_list_template = [
            'admin/%s/%s/editor/tree_editor.html' % (opts.app_label, opts.object_name.lower()),
            'admin/%s/editor/tree_editor.html' % opts.app_label,
            'admin/editor/tree_editor.html',
        ]
    
    def get_changelist(self, request, **kwargs):
        """
        Returns the ChangeList class for use on the changelist page.
        """
        return TreeChangeList
    
    def changelist_view(self, request, extra_context=None, *args, **kwargs):
        """
        Handle the changelist view, the django view for the model instances
        change list/actions page.
        """
        extra_context = extra_context or {}
        extra_context['EDITOR_MEDIA_PATH'] = settings.MEDIA_PATH
        extra_context['tree_structure'] = mark_safe(simplejson.dumps(
                                                    _build_tree_structure(self.model)))

        return super(TreeEditor, self).changelist_view(request, extra_context, *args, **kwargs)

    def _move_node(self, request):
        cut_item = self.model._tree_manager.get(pk=request.POST.get('cut_item'))
        pasted_on = self.model._tree_manager.get(pk=request.POST.get('pasted_on'))
        position = request.POST.get('position')

        if position in ('last-child', 'left'):
            self.model._tree_manager.move_node(cut_item, pasted_on, position)

            # Ensure that model save has been run
            source = self.model._tree_manager.get(pk=request.POST.get('cut_item'))
            source.save()

            return HttpResponse('OK')
        return HttpResponse('FAIL')

    def queryset(self, request):
        """
        Returns a QuerySet of all model instances that can be edited by the
        admin site. This is used by changelist_view.
        """
        # Use default ordering, always
        return self.model._default_manager.get_query_set()
