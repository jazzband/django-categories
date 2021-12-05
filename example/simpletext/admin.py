from django.contrib import admin

from categories.admin import CategoryBaseAdmin, CategoryBaseAdminForm

from .models import SimpleCategory, SimpleText


class SimpleTextAdmin(admin.ModelAdmin):
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
    class Meta:
        model = SimpleCategory
        fields = "__all__"


class SimpleCategoryAdmin(CategoryBaseAdmin):
    form = SimpleCategoryAdminForm


admin.site.register(SimpleText, SimpleTextAdmin)
admin.site.register(SimpleCategory, SimpleCategoryAdmin)
