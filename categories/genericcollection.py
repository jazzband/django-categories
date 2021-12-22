"""Special helpers for generic collections."""
import json

from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.urls import NoReverseMatch, reverse


class GenericCollectionInlineModelAdmin(admin.options.InlineModelAdmin):
    """Inline admin for generic model collections."""

    ct_field = "content_type"
    ct_fk_field = "object_id"

    def get_content_types(self):
        """Get the content types supported by this collection."""
        ctypes = ContentType.objects.all().order_by("id").values_list("id", "app_label", "model")
        elements = {}
        for x, y, z in ctypes:
            try:
                elements[x] = reverse("admin:%s_%s_changelist" % (y, z))
            except NoReverseMatch:
                continue
        return json.dumps(elements)

    def get_formset(self, request, obj=None, **kwargs):
        """Get the formset for the generic collection."""
        result = super(GenericCollectionInlineModelAdmin, self).get_formset(request, obj, **kwargs)
        result.content_types = self.get_content_types()
        result.ct_fk_field = self.ct_fk_field
        return result

    class Media:
        js = ("contentrelations/js/genericlookup.js",)


class GenericCollectionTabularInline(GenericCollectionInlineModelAdmin):
    """Tabular model admin for a generic collection."""

    template = "admin/edit_inline/gen_coll_tabular.html"


class GenericCollectionStackedInline(GenericCollectionInlineModelAdmin):
    """Stacked model admin for a generic collection."""

    template = "admin/edit_inline/gen_coll_stacked.html"
