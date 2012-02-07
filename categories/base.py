"""
This is the base class on which to build a hierarchical category-like model
with customizable metadata and its own name space.
"""

from django.contrib import admin
from django.db import models
from django import forms
from django.template.defaultfilters import slugify
from django.utils.encoding import force_unicode

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from mptt.managers import TreeManager

from .editor.tree_editor import TreeEditor
from .settings import ALLOW_SLUG_CHANGE, SLUG_TRANSLITERATOR

class CategoryManager(models.Manager):
    """
    A manager that adds an "active()" method for all active categories
    """
    def active(self):
        """
        Only categories that are active
        """
        return self.get_query_set().filter(active=True)


class CategoryBase(MPTTModel):
    """
    This base model includes the absolute bare bones fields and methods. One
    could simply subclass this model and do nothing else and it should work.
    """
    parent = TreeForeignKey('self', 
        blank=True, 
        null=True, 
        related_name="children", 
        verbose_name='Parent')
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    active = models.BooleanField(default=True)
    
    objects = CategoryManager()
    tree = TreeManager()
    
    def save(self, *args, **kwargs):
        """
        While you can activate an item without activating its descendants,
        It doesn't make sense that you can deactivate an item and have its 
        decendants remain active.
        """
        if not self.slug:
            self.slug = slugify(SLUG_TRANSLITERATOR(self.name))[:50]
        
        super(CategoryBase, self).save(*args, **kwargs)
        
        if not self.active:
            for item in self.get_descendants():
                if item.active != self.active:
                    item.active = self.active
                    item.save()
    
    def __unicode__(self):
        ancestors = self.get_ancestors()
        return ' > '.join([force_unicode(i.name) for i in ancestors]+[self.name,])
    
    class Meta:
        abstract = True
        unique_together = ('parent', 'name')
        ordering = ('tree_id', 'lft')
    
    class MPTTMeta:
        order_insertion_by = 'name'


class CategoryBaseAdminForm(forms.ModelForm):
    def clean_slug(self):
        if self.instance is None or not ALLOW_SLUG_CHANGE:
            self.cleaned_data['slug'] = slugify(self.cleaned_data['name'])
        return self.cleaned_data['slug'][:50]
    
    def clean(self):
        super(CategoryBaseAdminForm, self).clean()
        opts = self._meta
        
        # Validate slug is valid in that level
        kwargs = {}
        if self.cleaned_data.get('parent', None) is None:
            kwargs['parent__isnull'] = True
        else:
            kwargs['parent__pk'] = int(self.cleaned_data['parent'].id)
        this_level_slugs = [c['slug'] for c in opts.model.objects.filter(
                                **kwargs).values('id','slug'
                                ) if c['id'] != self.instance.id]
        if self.cleaned_data['slug'] in this_level_slugs:
            raise forms.ValidationError("The slug must be unique among "
                                        "the items at its level.")
        
        # Validate Category Parent
        # Make sure the category doesn't set itself or any of its children as 
        # its parent.
        decendant_ids = self.instance.get_descendants().values_list('id', flat=True)
        if self.cleaned_data.get('parent', None) is None or self.instance.id is None:
            return self.cleaned_data
        elif self.cleaned_data['parent'].id == self.instance.id:
            raise forms.ValidationError("You can't set the parent of the "
                                        "item to itself.")
        elif self.cleaned_data['parent'].id in decendant_ids:
            raise forms.ValidationError("You can't set the parent of the "
                                        "item to a descendant.")
        return self.cleaned_data


class CategoryBaseAdmin(TreeEditor, admin.ModelAdmin):
    form = CategoryBaseAdminForm
    list_display = ('name', 'active')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    
    actions = ['activate', 'deactivate']
    def get_actions(self, request):
        actions = super(CategoryBaseAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
    def deactivate(self, request, queryset):
        """
        Set active to False for selected items
        """
        opts = self._meta
        selected_cats = opts.model.objects.filter(
            pk__in=[int(x) for x in request.POST.getlist('_selected_action')])
        
        for item in selected_cats:
            if item.active:
                item.active = False
                item.save()
                item.children.all().update(active=False)
    deactivate.short_description = "Deactivate selected categories and their children"
    
    def activate(self, request, queryset):
        """
        Set active to True for selected items
        """
        opts = self._meta
        
        selected_cats = opts.model.objects.filter(
            pk__in=[int(x) for x in request.POST.getlist('_selected_action')])
        
        for item in selected_cats:
            item.active = True
            item.save()
            item.children.all().update(active=True)
    activate.short_description = "Activate selected categories and their children"
