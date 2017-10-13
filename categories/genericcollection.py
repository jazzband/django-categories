from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse, NoReverseMatch
import json


class GenericCollectionInlineModelAdmin(admin.options.InlineModelAdmin):
    ct_field = "content_type"
    ct_fk_field = "object_id"

    def get_content_types(self):
        ctypes = ContentType.objects.all().order_by('id').values_list('id', 'app_label', 'model')
        elements = {}
        for x, y, z in ctypes:
            try:
                elements[x] = reverse("admin:%s_%s_changelist" % (y, z))
            except NoReverseMatch:
                continue
        return json.dumps(elements)

    def get_formset(self, request, obj=None, **kwargs):
        result = super(GenericCollectionInlineModelAdmin, self).get_formset(request, obj, **kwargs)
        result.content_types = self.get_content_types()
        result.ct_fk_field = self.ct_fk_field
        return result

    class Media:
        js = ('contentrelations/js/genericlookup.js', )


class GenericCollectionTabularInline(GenericCollectionInlineModelAdmin):
    template = 'admin/edit_inline/gen_coll_tabular.html'


class GenericCollectionStackedInline(GenericCollectionInlineModelAdmin):
    template = 'admin/edit_inline/gen_coll_stacked.html'
