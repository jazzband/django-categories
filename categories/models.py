import re
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import force_unicode
import mptt

class CategoryTree(models.Model):
    """
    A group of categories that are all related under one tree.
    
    For example: Business, Movie Genre, Music Genre
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("categories_tree", args=[self.slug])


class Category(models.Model):
    category_tree = models.ForeignKey(CategoryTree, 
        blank=False, 
        null=False 
        related_name="categories")
    parent = models.ForeignKey('self', 
        blank=True, 
        null=True, 
        related_name="children", 
        help_text="Leave this blank for a top-level category", 
        verbose_name='Parent')
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    
    def get_absolute_url(self):
        """Return a path"""
        prefix = self.category_tree.get_absolute_url()
        ancestors = self.get_ancestors()
        return prefix + '/'.join([force_unicode(i.slug) for i in ancestors])
        
    class Meta:
        verbose_name_plural = 'categories'
        unique_together = (('parent', 'name'),)
        ordering = ('category_tree__name','parent__name','name')

    def __unicode__(self):
        ancestors = self.get_ancestors()
        return ' > '.join([force_unicode(i.name) for i in ancestors])

mptt.register(Category, order_insertion_by=['name'])
