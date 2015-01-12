from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

from .genericcollection import GenericCollectionTabularInline
from .settings import RELATION_MODELS, JAVASCRIPT_URL, REGISTER_ADMIN
from .models import Category
from .base import CategoryBaseAdminForm, CategoryBaseAdmin
from .settings import MODEL_REGISTRY, FIELD_REGISTRY


class NullTreeNodeChoiceField(forms.ModelChoiceField):
    """A ModelChoiceField for tree nodes."""
    def __init__(self, level_indicator=u'---', *args, **kwargs):
        self.level_indicator = level_indicator
        super(NullTreeNodeChoiceField, self).__init__(*args, **kwargs)

    def label_from_instance(self, obj):
        """
        Creates labels which represent the tree level of each node when
        generating option labels.
        """
        return u'%s %s' % (self.level_indicator * getattr(
                                        obj, obj._mptt_meta.level_attr), obj)
if RELATION_MODELS:
    from .models import CategoryRelation

    class InlineCategoryRelation(GenericCollectionTabularInline):
        model = CategoryRelation


class CategoryAdminForm(CategoryBaseAdminForm):
    class Meta:
        model = Category
        fields = "__all__"

    def clean_alternate_title(self):
        if self.instance is None or not self.cleaned_data['alternate_title']:
            return self.cleaned_data['name']
        else:
            return self.cleaned_data['alternate_title']


class CategoryAdmin(CategoryBaseAdmin):
    form = CategoryAdminForm
    list_display = ('name', 'alternate_title', 'active')
    fieldsets = (
        (None, {
            'fields': ('parent', 'name', 'thumbnail', 'active')
        }),
        (_('Meta Data'), {
            'fields': ('alternate_title', 'alternate_url', 'description',
                        'meta_keywords', 'meta_extra'),
            'classes': ('collapse',),
        }),
        (_('Advanced'), {
            'fields': ('order', 'slug'),
            'classes': ('collapse',),
        }),
    )

    if RELATION_MODELS:
        inlines = [InlineCategoryRelation, ]

    class Media:
        js = (JAVASCRIPT_URL + 'genericcollections.js',)

if REGISTER_ADMIN:
    admin.site.register(Category, CategoryAdmin)

model_regs = []
for key, value in MODEL_REGISTRY.items():
    for model in value:
        model_regs.append(model)

for model, modeladmin in admin.site._registry.items():
    if model in model_regs and modeladmin.fieldsets:
        fieldsets = tuple(getattr(modeladmin, 'fieldsets', ()))
        fields = [cat.split('.')[2] for cat in FIELD_REGISTRY if model in MODEL_REGISTRY[cat.split('.')[0]]]

        # if there are any fields left, add them under the categories fieldset
        if len(fields) > 0:
            admin.site.unregister(model)
            fieldsets += (('Categories', {
                    'fields': tuple(fields)
                }),)
            
            admin.site.register(model, type('newadmin', (modeladmin.__class__,), {
                'fieldsets': fieldsets
            }))
