from django.contrib import admin
from django.contrib.admin.options import TabularInline
from django import forms
from django.utils.translation import ugettext_lazy as _

from .genericcollection import GenericCollectionTabularInline
from .settings import RELATION_MODELS, JAVASCRIPT_URL, REGISTER_ADMIN
from .models import Category
from .base import CategoryBaseAdminForm, CategoryBaseAdmin
from .settings import MODEL_REGISTRY

from categories import models as category_models

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

    def clean_alternate_title(self):
        if self.instance is None or not self.cleaned_data['alternate_title']:
            return self.cleaned_data['name']
        else:
            return self.cleaned_data['alternate_title']

class CategorySponsorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategorySponsorForm, self).__init__(*args, **kwargs)
        self.fields['order'].widget = forms.HiddenInput()


class CategorySponsorInline(TabularInline):
    autocomplete_lookup_fields = {'fk': ['sponsorship']}
    extra = 1
    fields = ('sponsorship', 'url', 'order',)
    form = CategorySponsorForm
    model = category_models.CategorySponsor
    ordering = ('order',)
    raw_id_fields = ('sponsorship',)
    sortable_field_name = 'order'

class SponsoredCategoryListFilter(admin.SimpleListFilter):
    title = u'Sponsored'
    parameter_name = 'sponsored'

    def lookups(self, request, model_admin):
        return (
            ('sponsored', u'Sponsored'),
            ('unsponsored', u'Unsponsored'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'sponsored':
            return queryset.exclude(is_sponsored=True)
        if self.value() == 'unsponsored':
            return queryset.filter(is_sponsored=False)
        return queryset

class CategoryAdmin(CategoryBaseAdmin):
    form = CategoryAdminForm
    list_display = ('name', 'alternate_title', 'active', 'view_is_sponsored')
    fieldsets = (
        (None, {
            'fields': ('parent', 'name', 'thumbnail', 'mobile_thumbnail', 'is_sponsored', 'active')
        }),
        (_('Meta Data'), {
            'fields': ('alternate_title', 'alternate_url', 'description',
                        'meta_keywords', 'meta_extra'),
            'classes': ('grp-collapse',),
        }),
        (_('Advanced'), {
            'fields': ('order', 'slug'),
            'classes': ('grp-collapse',),
        }),
    )

    inlines = (CategorySponsorInline,)

    list_filter = (
        SponsoredCategoryListFilter,
    )

    class Media:
        js = (JAVASCRIPT_URL + 'genericcollections.js',)
        css = {
            "all": (
                'admin/categories/css/categories.css',
            ),
        }

    def save_formset(self, request, form, formset, change):
        # Save the formset (including all related/many-to-many objects)
        formset.save()

        obj = form.instance

        # Set is_sponsored = True if any sponsors were associated with this category
        if obj.sponsorships.count() > 0:
            obj.is_sponsored = True

        # Save the parent object with the newly assigned value for is_sponsored
        obj.save()

    # Enables display of boolean value for is_sponsored in list_display
    def view_is_sponsored(self, obj):
        return obj.is_sponsored
    view_is_sponsored.boolean = True
    view_is_sponsored.short_description = u"is sponsored"

admin.site.register(Category, CategoryAdmin)

for model, modeladmin in admin.site._registry.items():
    if model in MODEL_REGISTRY.values() and modeladmin.fieldsets:
        fieldsets = getattr(modeladmin, 'fieldsets', ())
        fields = [cat.split('.')[2] for cat in MODEL_REGISTRY if MODEL_REGISTRY[cat] == model]
        # check each field to see if already defined
        for cat in fields:
            for k, v in fieldsets:
                if cat in v['fields']:
                    fields.remove(cat)
        # if there are any fields left, add them under the categories fieldset
        if len(fields) > 0:
            admin.site.unregister(model)
            admin.site.register(model, type('newadmin', (modeladmin.__class__,), {
                'fieldsets': fieldsets + (('Categories', {
                    'fields': fields
                }),)
            }))
