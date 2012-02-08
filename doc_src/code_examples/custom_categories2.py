from django.contrib import admin

from categories.admin import CategoryBaseAdmin, CategoryBaseAdminForm

from .models import SimpleCategory

class SimpleCategoryAdminForm(CategoryBaseAdminForm):
    class Meta:
        model = SimpleCategory

class SimpleCategoryAdmin(CategoryBaseAdmin):
    form = SimpleCategoryAdminForm

admin.site.register(SimpleCategory, SimpleCategoryAdmin)