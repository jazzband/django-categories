from django.contrib import admin
from django import forms
from django.template.defaultfilters import slugify

from genericcollection import GenericCollectionTabularInline

from .settings import ALLOW_SLUG_CHANGE, RELATION_MODELS, JAVASCRIPT_URL
from .editor.tree_editor import TreeEditor
from .models import Category
from categories import model_registry


class NullTreeNodeChoiceField(forms.ModelChoiceField):
    """A ModelChoiceField for tree nodes."""
    def __init__(self, level_indicator=u'---', *args, **kwargs):
        self.level_indicator = level_indicator
        #kwargs['empty_label'] = None
        super(NullTreeNodeChoiceField, self).__init__(*args, **kwargs)

    def label_from_instance(self, obj):
        """
        Creates labels which represent the tree level of each node when
        generating option labels.
        """
        return u'%s %s' % (self.level_indicator * getattr(obj, obj._meta.level_attr),
                                obj)
if RELATION_MODELS:
    from models import CategoryRelation

    class InlineCategoryRelation(GenericCollectionTabularInline):
        model = CategoryRelation


class CategoryAdminForm(forms.ModelForm):
    parent = NullTreeNodeChoiceField(queryset=Category.tree.all(), 
                                 level_indicator=u'+-', 
                                 empty_label='------', 
                                 required=False)
    class Meta:
        model = Category
    
    def clean_slug(self):
        if self.instance is None or not ALLOW_SLUG_CHANGE:
            self.cleaned_data['slug'] = slugify(self.cleaned_data['name'])
        return self.cleaned_data['slug'][:50]
    
    def clean_alternate_title(self):
        if self.instance is None or not self.cleaned_data['alternate_title']:
            return self.cleaned_data['name']
        else:
            return self.cleaned_data['alternate_title']
    
    def clean(self):
        super(CategoryAdminForm, self).clean()
        
        # Validate slug is valid in that level
        kwargs = {}
        if self.cleaned_data.get('parent', None) is None:
            kwargs['parent__isnull'] = True
        else:
            kwargs['parent__pk'] = int(self.cleaned_data['parent'].id)
        this_level_slugs = [c['slug'] for c in Category.objects.filter(**kwargs).values('id','slug') if c['id'] != self.instance.id]
        if self.cleaned_data['slug'] in this_level_slugs:
            raise forms.ValidationError("A category slug must be unique among"
                                        "categories at its level.")
        
        # Validate Category Parent
        # Make sure the category doesn't set itself or any of its children as its parent."
        if self.cleaned_data.get('parent', None) is None or self.instance.id is None:
            return self.cleaned_data
        elif self.cleaned_data['parent'].id == self.instance.id:
            raise forms.ValidationError("You can't set the parent of the "
                                        "category to itself.")
        elif self.cleaned_data['parent'].id in [i[0] for i in self.instance.get_descendants().values_list('id')]:
            raise forms.ValidationError("You can't set the parent of the "
                                        "category to a descendant.")
        return self.cleaned_data


class CategoryAdmin(TreeEditor, admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = ('name', 'alternate_title', 'active')
    search_fields = ('name', 'alternate_title', )
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {
            'fields': ('parent', 'name', 'thumbnail', 'active')
        }),
        ('Meta Data', {
            'fields': ('alternate_title', 'alternate_url', 'description', 
                        'meta_keywords', 'meta_extra'),
            'classes': ('collapse',),
        }),
        ('Advanced', {
            'fields': ('order', 'slug'),
            'classes': ('collapse',),
        }),
    )
    
    actions = ['activate', 'deactivate']
    def get_actions(self, request):
        actions = super(CategoryAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
    def deactivate(self, request, queryset):
        """
        Set active to False for selected items
        """
        selected_cats = Category.objects.filter(
            pk__in=[int(x) for x in request.POST.getlist('_selected_action')])
        
        for item in selected_cats:
            if item.active:
                item.active = False
                item.save()
                item.children.all().update(active=False)
    deactivate.short_description = "Deactivate selected categories and their children"
    
    def activate(self, request, queryset):
        """
        Set active to True for selected items
        """
        selected_cats = Category.objects.filter(
            pk__in=[int(x) for x in request.POST.getlist('_selected_action')])
        
        for item in selected_cats:
            item.active = True
            item.save()
            item.children.all().update(active=True)
    activate.short_description = "Activate selected categories and their children"
    
    if RELATION_MODELS:
        inlines = [InlineCategoryRelation,]
    
    class Media:
        js = (JAVASCRIPT_URL + 'genericcollections.js',)

admin.site.register(Category, CategoryAdmin)

for model, modeladmin in admin.site._registry.items():
    if model in model_registry.values() and modeladmin.fieldsets:
        fieldsets = getattr(modeladmin, 'fieldsets', ())
        fields = [cat.split('.')[2] for cat in model_registry if model_registry[cat] == model]
        # check each field to see if already defined
        for cat in fields:
            for k, v in fieldsets:
                if cat in v['fields']:
                    fields.remove(cat)
        # if there are any fields left, add them under the categories fieldset
        if len(fields) > 0:
            print fields
            admin.site.unregister(model)
            admin.site.register(model, type('newadmin', (modeladmin.__class__,), {
                'fieldsets': fieldsets + (('Categories', {
                    'fields': fields
                }),)
            }))
