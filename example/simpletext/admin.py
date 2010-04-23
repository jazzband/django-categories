from models import SimpleText
from django.contrib import admin


class SimpleTextAdmin(admin.ModelAdmin):
    filter_horizontal = ['cats',]


admin.site.register(SimpleText, SimpleTextAdmin)