from django.contrib import admin
from django.db.models.query import QuerySet
from django.contrib.admin.views.main import ChangeList
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.options import IncorrectLookupParameters
from django import template
from django.shortcuts import render_to_response

import django

import settings

class TreeEditorQuerySet(QuerySet):
    """
    The TreeEditorQuerySet is a special query set used only in the TreeEditor
    ChangeList page. The only difference to a regular QuerySet is that it
    will enforce:
    
        (a) The result is ordered in correct tree order so that
            the TreeAdmin works all right.
            
        (b) It ensures that all ancestors of selected items are included
            in the result set, so the resulting tree display actually
            makes sense.
    """
    def iterator(self):
        qs = self
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
            for p in super(TreeEditorQuerySet, self.order_by('rght')).iterator():
                if p.parent_id and p.parent_id not in include_pages and \
                                   p.id not in include_pages:
                    ancestor_id_list = p.get_ancestors().values_list('id', flat=True)
                    include_pages.update(ancestor_id_list)
            
            if include_pages:
                qs = qs | self.model._default_manager.filter(id__in=include_pages)
            
            qs = qs.distinct()
            
        for obj in super(TreeEditorQuerySet, qs).iterator():
            yield obj
    
    # Although slicing isn't nice in a tree, it is used in the deletion action
    #  in the admin changelist. This causes github issue #25
    # def __getitem__(self, index):
    #     return self   # Don't even try to slice
    
    def get(self, *args, **kwargs):
        """
        Quick and dirty hack to fix change_view and delete_view; they use
        self.queryset(request).get(...) to get the object they should work
        with. Our modifications to the queryset when INCLUDE_ANCESTORS is
        enabled make get() fail often with a MultipleObjectsReturned
        exception.
        """
        return self.model._default_manager.get(*args, **kwargs)

class TreeChangeList(ChangeList):
    def __init__(self, request, model, list_display, list_display_links,
            list_filter, date_hierarchy, search_fields, list_select_related,
            list_per_page, list_max_show_all, list_editable, model_admin):
        if django.VERSION[1] < 4:
            super(TreeChangeList, self).__init__(request, model, list_display, 
                list_display_links, list_filter, date_hierarchy, search_fields, 
                list_select_related, list_per_page, list_editable, model_admin)
        else:
            super(TreeChangeList, self).__init__(request, model, list_display, 
                list_display_links, list_filter, date_hierarchy, search_fields, 
                list_select_related, list_per_page, list_max_show_all, 
                list_editable, model_admin)
        
    def _get_default_ordering(self):
        return [] #'', '' #('tree_id', 'lft')
    
    def get_ordering(self, request=None):
        return [] #'', '' #('tree_id', 'lft')
    
    def get_query_set(self, *args, **kwargs):
        qs = super(TreeChangeList, self).get_query_set(*args, **kwargs).order_by('tree_id', 'lft')
        return qs

class TreeEditor(admin.ModelAdmin):
    list_per_page = 999999999 # We can't have pagination
    list_max_show_all = 200 # new in django 1.4
    
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
    
    def old_changelist_view(self, request, extra_context=None):
        "The 'change list' admin view for this model."
        from django.contrib.admin.views.main import ERROR_FLAG
        from django.core.exceptions import PermissionDenied
        from django.utils.encoding import force_unicode
        from django.utils.translation import ungettext
        opts = self.model._meta
        app_label = opts.app_label
        if not self.has_change_permission(request, None):
            raise PermissionDenied

        # Check actions to see if any are available on this changelist
        actions = self.get_actions(request)

        # Remove action checkboxes if there aren't any actions available.
        list_display = list(self.list_display)
        if not actions:
            try:
                list_display.remove('action_checkbox')
            except ValueError:
                pass

        try:
            cl = TreeChangeList(request, self.model, list_display, 
                self.list_display_links, self.list_filter, self.date_hierarchy, 
                self.search_fields, self.list_select_related, 
                self.list_per_page, self.list_max_show_all, 
                self.list_editable, self)
        except IncorrectLookupParameters:
            # Wacky lookup parameters were given, so redirect to the main
            # changelist page, without parameters, and pass an 'invalid=1'
            # parameter via the query string. If wacky parameters were given and
            # the 'invalid=1' parameter was already in the query string, something
            # is screwed up with the database, so display an error page.
            if ERROR_FLAG in request.GET.keys():
                return render_to_response(
                    'admin/invalid_setup.html', {'title': _('Database error')})
            return HttpResponseRedirect(request.path + '?' + ERROR_FLAG + '=1')

        # If the request was POSTed, this might be a bulk action or a bulk edit.
        # Try to look up an action first, but if this isn't an action the POST
        # will fall through to the bulk edit check, below.
        if actions and request.method == 'POST':
            response = self.response_action(request, queryset=cl.get_query_set())
            if response:
                return response

        # If we're allowing changelist editing, we need to construct a formset
        # for the changelist given all the fields to be edited. Then we'll
        # use the formset to validate/process POSTed data.
        formset = cl.formset = None

        # Handle POSTed bulk-edit data.
        if request.method == "POST" and self.list_editable:
            FormSet = self.get_changelist_formset(request)
            formset = cl.formset = FormSet(
                request.POST, request.FILES, queryset=cl.result_list
            )
            if formset.is_valid():
                changecount = 0
                for form in formset.forms:
                    if form.has_changed():
                        obj = self.save_form(request, form, change=True)
                        self.save_model(request, obj, form, change=True)
                        form.save_m2m()
                        change_msg = self.construct_change_message(request, form, None)
                        self.log_change(request, obj, change_msg)
                        changecount += 1

                if changecount:
                    if changecount == 1:
                        name = force_unicode(opts.verbose_name)
                    else:
                        name = force_unicode(opts.verbose_name_plural)
                    msg = ungettext(
                        "%(count)s %(name)s was changed successfully.",
                        "%(count)s %(name)s were changed successfully.",
                        changecount) % {'count': changecount,
                                        'name': name,
                                        'obj': force_unicode(obj)}
                    self.message_user(request, msg)

                return HttpResponseRedirect(request.get_full_path())

        # Handle GET -- construct a formset for display.
        elif self.list_editable:
            FormSet = self.get_changelist_formset(request)
            formset = cl.formset = FormSet(queryset=cl.result_list)

        # Build the list of media to be used by the formset.
        if formset:
            media = self.media + formset.media
        else:
            media = self.media

        # Build the action form and populate it with available actions.
        if actions:
            action_form = self.action_form(auto_id=None)
            action_form.fields['action'].choices = self.get_action_choices(request)
        else:
            action_form = None

        context = {
            'title': cl.title,
            'is_popup': cl.is_popup,
            'cl': cl,
            'media': media,
            'has_add_permission': self.has_add_permission(request),
            'app_label': app_label,
            'action_form': action_form,
            'actions_on_top': self.actions_on_top,
            'actions_on_bottom': self.actions_on_bottom,
        }
        if django.VERSION[1] < 4:
            context['root_path'] = self.admin_site.root_path
        else:
            selection_note_all = ungettext('%(total_count)s selected',
                'All %(total_count)s selected', cl.result_count)
            
            context.update({
                'module_name': force_unicode(opts.verbose_name_plural),
                'selection_note': _('0 of %(cnt)s selected') % {'cnt': len(cl.result_list)},
                'selection_note_all': selection_note_all % {'total_count': cl.result_count},
            })
        context.update(extra_context or {})
        context_instance = template.RequestContext(
            request, current_app=self.admin_site.name
        )
        return render_to_response(self.change_list_template or [
            'admin/%s/%s/change_list.html' % (app_label, opts.object_name.lower()),
            'admin/%s/change_list.html' % app_label,
            'admin/change_list.html'
        ], context, context_instance=context_instance)
    
    def changelist_view(self, request, extra_context=None, *args, **kwargs):
        """
        Handle the changelist view, the django view for the model instances
        change list/actions page.
        """
        extra_context = extra_context or {}
        extra_context['EDITOR_MEDIA_PATH'] = settings.MEDIA_PATH
        extra_context['EDITOR_TREE_INITIAL_STATE'] = settings.TREE_INITIAL_STATE
        if django.VERSION[1] >= 2:
            return super(TreeEditor, self).changelist_view(
                                    request, extra_context, *args, **kwargs)
        else:
            return self.old_changelist_view(request, extra_context)
    
    def queryset(self, request):
        """
        Returns a QuerySet of all model instances that can be edited by the
        admin site. This is used by changelist_view.
        """
        qs = self.model._default_manager.get_query_set()
        qs.__class__ = TreeEditorQuerySet
        return qs
