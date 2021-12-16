"""Admin interface classes."""
from django import forms
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .base import CategoryBaseAdmin, CategoryBaseAdminForm
from .genericcollection import GenericCollectionTabularInline
from .models import Category
from .settings import JAVASCRIPT_URL, MODEL_REGISTRY, REGISTER_ADMIN, RELATION_MODELS


class NullTreeNodeChoiceField(forms.ModelChoiceField):
    """A ModelChoiceField for tree nodes."""

    def __init__(self, level_indicator="---", *args, **kwargs):
        self.level_indicator = level_indicator
        super(NullTreeNodeChoiceField, self).__init__(*args, **kwargs)

    def label_from_instance(self, obj) -> str:
        """
        Creates labels which represent the tree level of each node when generating option labels.
        """
        return "%s %s" % (self.level_indicator * getattr(obj, obj._mptt_meta.level_attr), obj)


if RELATION_MODELS:
    from .models import CategoryRelation

    class InlineCategoryRelation(GenericCollectionTabularInline):
        """The inline admin panel for category relations."""

        model = CategoryRelation


class CategoryAdminForm(CategoryBaseAdminForm):
    """The form for a category in the admin."""

    class Meta:
        model = Category
        fields = "__all__"

    def clean_alternate_title(self) -> str:
        """Return either the name or alternate title for the category."""
        if self.instance is None or not self.cleaned_data["alternate_title"]:
            return self.cleaned_data["name"]
        else:
            return self.cleaned_data["alternate_title"]


class CategoryAdmin(CategoryBaseAdmin):
    """Admin for categories."""

    form = CategoryAdminForm
    list_display = ("name", "alternate_title", "active")
    fieldsets = (
        (None, {"fields": ("parent", "name", "thumbnail", "active")}),
        (
            _("Meta Data"),
            {
                "fields": ("alternate_title", "alternate_url", "description", "meta_keywords", "meta_extra"),
                "classes": ("collapse",),
            },
        ),
        (
            _("Advanced"),
            {
                "fields": ("order", "slug"),
                "classes": ("collapse",),
            },
        ),
    )

    if RELATION_MODELS:
        inlines = [
            InlineCategoryRelation,
        ]

    class Media:
        js = (JAVASCRIPT_URL + "genericcollections.js",)


if REGISTER_ADMIN:
    admin.site.register(Category, CategoryAdmin)

for model, modeladmin in list(admin.site._registry.items()):
    if model in list(MODEL_REGISTRY.values()) and modeladmin.fieldsets:
        fieldsets = getattr(modeladmin, "fieldsets", ())
        fields = [cat.split(".")[2] for cat in MODEL_REGISTRY if MODEL_REGISTRY[cat] == model]
        # check each field to see if already defined
        for cat in fields:
            for k, v in fieldsets:
                if cat in v["fields"]:
                    fields.remove(cat)
        # if there are any fields left, add them under the categories fieldset
        if len(fields) > 0:
            admin.site.unregister(model)
            admin.site.register(
                model,
                type(
                    "newadmin",
                    (modeladmin.__class__,),
                    {"fieldsets": fieldsets + (("Categories", {"fields": fields}),)},
                ),
            )
