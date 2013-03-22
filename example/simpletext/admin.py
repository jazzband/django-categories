from models import SimpleText, SimpleCategory
from django.contrib import admin

from categories.admin import CategoryBaseAdmin, CategoryBaseAdminForm

# class SimpleTextAdmin(admin.ModelAdmin):
#     filter_horizontal = ['cats',]
# 

class SimpleCategoryAdminForm(CategoryBaseAdminForm):
    class Meta:
        model = SimpleCategory

class SimpleCategoryAdmin(CategoryBaseAdmin):
    form = SimpleCategoryAdminForm
    
admin.site.register(SimpleText) #, SimpleTextAdmin)
admin.site.register(SimpleCategory, SimpleCategoryAdmin)