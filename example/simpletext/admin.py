from .models import SimpleText, SimpleCategory
from django.contrib import admin

from categories.admin import CategoryBaseAdmin, CategoryBaseAdminForm


class SimpleTextAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'description', )
        }),
    )


class SimpleCategoryAdminForm(CategoryBaseAdminForm):
    class Meta:
        model = SimpleCategory
        fields = '__all__'


class SimpleCategoryAdmin(CategoryBaseAdmin):
    form = SimpleCategoryAdminForm

admin.site.register(SimpleText, SimpleTextAdmin)
admin.site.register(SimpleCategory, SimpleCategoryAdmin)
