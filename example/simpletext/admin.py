"""Admin interface for simple text."""
from django.contrib import admin

from categories.admin import CategoryBaseAdmin, CategoryBaseAdminForm

from .models import SimpleCategory, SimpleText


class SimpleTextAdmin(admin.ModelAdmin):
    """Admin for simple text model."""

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "description",
                )
            },
        ),
    )


class SimpleCategoryAdminForm(CategoryBaseAdminForm):
    """Admin form for simple category."""

    class Meta:
        model = SimpleCategory
        fields = "__all__"


class SimpleCategoryAdmin(CategoryBaseAdmin):
    """Admin for simple category."""

    form = SimpleCategoryAdminForm


admin.site.register(SimpleText, SimpleTextAdmin)
admin.site.register(SimpleCategory, SimpleCategoryAdmin)
