from django.contrib import admin
from django import forms
from django.template.defaultfilters import slugify

from mptt.forms import TreeNodeChoiceField
from editor.tree_editor import TreeEditor
from genericcollection import GenericCollectionTabularInline

from settings import ALLOW_SLUG_CHANGE, RELATION_MODELS
from categories import registry
from models import Category

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
        return self.cleaned_data['slug']
    
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
            raise forms.ValidationError("A category slug must be unique among categories at its level.")
        
        # Validate Category Parent
        # Make sure the category doesn't set itself or any of its children as its parent."
        if self.cleaned_data.get('parent', None) is None or self.instance.id is None:
            return self.cleaned_data
        elif self.cleaned_data['parent'].id == self.instance.id:
            raise forms.ValidationError("You can't set the parent of the category to itself.")
        elif self.cleaned_data['parent'].id in [i[0] for i in self.instance.get_descendants().values_list('id')]:
            raise forms.ValidationError("You can't set the parent of the category to a descendant.")
        return self.cleaned_data


class CategoryAdmin(TreeEditor, admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = ('name','order','alternate_title',)
    search_fields = (('name',))
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {
            'fields': ('parent', 'name')
        }),
        ('Meta Data', {
            'fields': ('alternate_title', 'description', 'meta_keywords', 'meta_extra'),
            'classes': ('collapse',),
        }),
        ('Advanced', {
            'fields': ('order', 'slug'),
            'classes': ('collapse',),
        }),
    )
    if RELATION_MODELS:
        inlines = [InlineCategoryRelation,]
    
    class Media:
        js = ('js/genericcollections.js',)
    

admin.site.register(Category, CategoryAdmin)

for model,modeladmin in admin.site._registry.items():
    if model in registry.values() and modeladmin.fieldsets:
        fieldsets = getattr(modeladmin, 'fieldsets', ())
        fields = [cat.split('.')[1] for cat in registry]
        # check each field to see if already defined
        for cat in fields:
            for k,v in fieldsets:
                if cat in v['fields']:
                    fields.remove(cat)
        # if there are any fields left, add them under the categories fieldset
        if len(fields) > 0:
            admin.site.unregister(model)
            admin.site.register(model, type('newadmin', (modeladmin.__class__,), {
                'fieldsets': fieldsets + (('Categories',{
                    'fields': fields
                }),)
            }))