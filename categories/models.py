from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import force_unicode
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core.files.storage import get_storage_class
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext as _

from mptt.models import MPTTModel

from .settings import (RELATION_MODELS, RELATIONS, THUMBNAIL_UPLOAD_PATH, 
                        THUMBNAIL_STORAGE)

STORAGE = get_storage_class(THUMBNAIL_STORAGE)

class CategoryManager(models.Manager):
    """
    A manager that adds an "active()" method for all active categories
    """
    def active(self):
        """
        Only categories that are active
        """
        return self.get_query_set().filter(active=True)

class Category(MPTTModel):
    parent = models.ForeignKey('self', 
        blank=True, 
        null=True, 
        related_name="children", 
        help_text="Leave this blank for an Category Tree", 
        verbose_name='Parent')
    name = models.CharField(max_length=100)
    thumbnail = models.FileField(
        upload_to=THUMBNAIL_UPLOAD_PATH, 
        null=True, blank=True,
        storage=STORAGE(),)
    thumbnail_width = models.IntegerField(blank=True, null=True)
    thumbnail_height = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    slug = models.SlugField()
    alternate_title = models.CharField(
        blank=True,
        default="",
        max_length=100,
        help_text="An alternative title to use on pages with this category.")
    alternate_url = models.CharField(
        blank=True, 
        max_length=200, 
        help_text="An alternative URL to use instead of the one derived from the category hierarchy.")
    description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(
        blank=True,
        default="",
        max_length=255,
        help_text="Comma-separated keywords for search engines.")
    meta_extra = models.TextField(
        blank=True,
        default="",
        help_text="(Advanced) Any additional HTML to be placed verbatim in the &lt;head&gt;")
    active = models.BooleanField(default=True)
    
    objects = CategoryManager()
    
    @property
    def short_title(self):
        return self.name
    
    def get_absolute_url(self):
        """Return a path"""
        if self.alternate_url:
            return self.alternate_url
        prefix = reverse('categories_tree_list')
        ancestors = list(self.get_ancestors()) + [self,]
        return prefix + '/'.join([force_unicode(i.slug) for i in ancestors]) + '/'
    
    if RELATION_MODELS:
        def get_related_content_type(self, content_type):
            """
            Get all related items of the specified content type
            """
            return self.categoryrelation_set.filter(
                content_type__name=content_type)
        
        def get_relation_type(self, relation_type):
            """
            Get all relations of the specified relation type
            """
            return self.categoryrelation_set.filter(relation_type=relation_type)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:50]
        if self.thumbnail:
            from django.core.files.images import get_image_dimensions
            import django
            if django.VERSION[1] < 2:
                width, height = get_image_dimensions(self.thumbnail.file)
            else:
                width, height = get_image_dimensions(self.thumbnail.file, close=True)
        else:
            width, height = None, None
        
        self.thumbnail_width = width
        self.thumbnail_height = height
        
        super(Category, self).save(*args, **kwargs)
        
        # While you can activate an item without activating its descendants,
        # It doesn't make sense that you can deactivate an item and have its 
        # decendants remain active.
        if not self.active:
            for item in self.get_descendants():
                if item.active != self.active:
                    item.active = self.active
                    item.save()
    
    class Meta:
        verbose_name_plural = 'categories'
        unique_together = ('parent', 'name')
        ordering = ('tree_id', 'lft')
    
    class MPTTMeta:
        verbose_name_plural = 'categories'
        unique_together = ('parent', 'name')
        ordering = ('tree_id', 'lft')
        order_insertion_by = 'name'
    
    def __unicode__(self):
        ancestors = self.get_ancestors()
        return ' > '.join([force_unicode(i.name) for i in ancestors]+[self.name,])

if RELATION_MODELS:
    category_relation_limits = reduce(lambda x,y: x|y, RELATIONS)
    class CategoryRelationManager(models.Manager):
        def get_content_type(self, content_type):
            qs = self.get_query_set()
            return qs.filter(content_type__name=content_type)
        
        def get_relation_type(self, relation_type):
            qs = self.get_query_set()
            return qs.filter(relation_type=relation_type)
    
    class CategoryRelation(models.Model):
        """Related story item"""
        story = models.ForeignKey(Category)
        content_type = models.ForeignKey(
            ContentType, limit_choices_to=category_relation_limits)
        object_id = models.PositiveIntegerField()
        content_object = generic.GenericForeignKey('content_type', 'object_id')
        relation_type = models.CharField(_("Relation Type"), 
            max_length="200", 
            blank=True, 
            null=True,
            help_text=_("A generic text field to tag a relation, like 'leadphoto'."))
        
        objects = CategoryRelationManager()
        
        def __unicode__(self):
            return u"CategoryRelation"
