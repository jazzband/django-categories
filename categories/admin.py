from ellington.categories.models import Hierarchy, Category, Alias
from django.contrib import admin
from django import forms
from ellington.core.forms import RequiredModelForm

class CategoryAdminForm(RequiredModelForm):
    required_if_other_not_given = {
        'hierarchy': 'parent',
        'parent': 'hierarchy',
    }
    
    class Meta:
        model = Category

    def clean_name(self):
        if '/' in self.cleaned_data['name']:
            raise forms.ValidationError, "A category name can't contain slashes."
        return self.cleaned_data['name']

    def clean(self):
        super(CategoryAdminForm, self).clean()
        
        if 'slug' in self.cleaned_data and 'parent' in self.cleaned_data and 'hierarchy' in self.cleaned_data:
            if self.cleaned_data['parent'] is not None:
                # inherit from parent
                self.cleaned_data['hierarchy'] = self.cleaned_data['parent'].hierarchy

            #Validate slug
            kwargs = {}
            if self.cleaned_data.get('hierarchy', False):
                kwargs['hierarchy__pk'] = int(self.cleaned_data['hierarchy'].id)
                kwargs['parent__isnull'] = True
            else:
                kwargs['parent__pk'] = int(self.cleaned_data['parent'].id)
            this_level_slugs = [c.slug for c in Category.objects.filter(**kwargs) if c.id != self.cleaned_data.get("id", None)]
            if self.cleaned_data['slug'] in this_level_slugs:
                raise forms.ValidationError("A category slug must be unique among categories at its level.")

            #Validate Category Parent
            "Makes sure the category doesn't set itself or any of its children as its parent."
            if not self.cleaned_data['parent']:
                return self.cleaned_data

            p_data = int(self.cleaned_data['parent'].pk)
            h_data = self.cleaned_data.get('hierarchy', False)
            if h_data:
                h_data = int(h_data.pk)
            if p_data and h_data:
                p = Category.objects.get(pk=p_data)
                if p.hierarchy_id != h_data:
                    raise forms.ValidationError("This parent is not within the selected hierarchy.")

            # Check that the parent isn't a child of this category
            # Requires that we look up "this" object; if it doesn't exist
            # we can assume we're at the add stage and return
            this_id = self.cleaned_data.get("id", None)
            if not this_id:
                return self.cleaned_data

            try:
                selected_parent = Category.objects.get(pk=p_data)
            except Category.DoesNotExist:
                return self.cleaned_data

            if selected_parent.id == this_id:
                raise forms.ValidationError("A category can't be its own parent.")

            try:
                this_category = Category.objects.get(pk=p_data)
            except Category.DoesNotExist:
                return self.cleaned_data

            for c in this_category.get_all_children():
                if c.id == this_id:
                    raise forms.ValidationError("A category can't set a child category to be its own parent.")
            return self.cleaned_data
        else:
            raise forms.ValidationError("Cannot clean data")


class CategoryAdmin(admin.ModelAdmin):
    form=CategoryAdminForm
    fields = ('hierarchy', 'parent', 'name', 'slug')
    list_display = ('__unicode__',)
    list_filter = ('hierarchy',)
    search_fields = ('name', 'path')
    prepopulated_fields = {'slug': ('name',)}


class HierarchyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class AliasAdmin(admin.ModelAdmin):
    list_display = ['category', 'parent']
    search_fields = ['category__name', 'parent__name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Hierarchy, HierarchyAdmin)
admin.site.register(Alias, AliasAdmin)
