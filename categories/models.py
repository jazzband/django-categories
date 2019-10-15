from django.core.files.images import get_image_dimensions
from wiki.models import Article
from django.urls import reverse
from django.db import models
from django.utils.encoding import force_text
from django.contrib.contenttypes.models import ContentType
from functools import reduce
try:
    from django.contrib.contenttypes.fields import GenericForeignKey
except ImportError:
    from django.contrib.contenttypes.generic import GenericForeignKey
from django.core.files.storage import get_storage_class

from django.utils.translation import ugettext_lazy as _

from .settings import (RELATION_MODELS, RELATIONS, THUMBNAIL_UPLOAD_PATH, THUMBNAIL_STORAGE)

from .base import CategoryBase

STORAGE = get_storage_class(THUMBNAIL_STORAGE)

class Category(CategoryBase):
    thumbnail = models.FileField(
        upload_to=THUMBNAIL_UPLOAD_PATH,
        null=True, blank=True,
        storage=STORAGE(),)
    thumbnail_width = models.IntegerField(blank=True, null=True)
    thumbnail_height = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(default=0)
    alternate_title = models.CharField(
        blank=True,
        default="",
        max_length=100,
        help_text="An alternative title to use on pages with this category.")
    alternate_url = models.CharField(
        blank=True,
        max_length=200,
        help_text="An alternative URL to use instead of the one derived from "
                  "the category hierarchy.")
    description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(
        blank=True,
        default="",
        max_length=255,
        help_text="Comma-separated keywords for search engines.")
    meta_extra = models.TextField(
        blank=True,
        default="",
        help_text="(Advanced) Any additional HTML to be placed verbatim "
                  "in the &lt;head&gt;")

    @property
    def short_title(self):
        return self.name

    def get_absolute_url(self):
        """Return a path"""
        from django.urls import NoReverseMatch

        if self.alternate_url:
            return self.alternate_url
        try:
            prefix = reverse('categories_tree_list')
        except NoReverseMatch:
            prefix = '/'
        ancestors = list(self.get_ancestors()) + [self, ]
        return prefix + '/'.join([force_text(i.slug) for i in ancestors]) + '/'

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
        if self.thumbnail:
            width, height = get_image_dimensions(self.thumbnail.file, close=True)
        else:
            width, height = None, None

        self.thumbnail_width = width
        self.thumbnail_height = height

        super(Category, self).save(*args, **kwargs)

    class Meta(CategoryBase.Meta):
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    class MPTTMeta:
        order_insertion_by = ('order', 'name')

class ArticleCategory(CategoryBase):
    """
    Category with an associated article landing page.
    """
    # the landing page article
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=False, related_name='category+')
    # articles in the category
    member_articles = models.ManyToManyField(Article, related_name="categories+", blank=True, related_query_name="categories+")
    # category description
    description = models.TextField(blank=True, null=True)

    @property
    def short_title(self):
        return self.name

    def subtree_ids(self):
        """Return a list containing the ID of this category and all its subcategories"""
        queue = [self]
        ids = [] # IDs of inheriting categories
        while queue:
            child = queue.pop()
            ids.append(child.id)
            queue.extend(child.children.all())
        return ids

    class Meta(CategoryBase.Meta):
        verbose_name = _('article category')
        verbose_name_plural = _('article categories')

if RELATIONS:
    CATEGORY_RELATION_LIMITS = reduce(lambda x, y: x | y, RELATIONS)
else:
    CATEGORY_RELATION_LIMITS = []


class CategoryRelationManager(models.Manager):
    def get_content_type(self, content_type):
        """
        Get all the items of the given content type related to this item.
        """
        qs = self.get_queryset()
        return qs.filter(content_type__name=content_type)

    def get_relation_type(self, relation_type):
        """
        Get all the items of the given relationship type related to this item.
        """
        qs = self.get_queryset()
        return qs.filter(relation_type=relation_type)


class CategoryRelation(models.Model):
    """Related category item"""
    category = models.ForeignKey(Category, verbose_name=_('category'), on_delete=models.CASCADE)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, limit_choices_to=CATEGORY_RELATION_LIMITS,
        verbose_name=_('content type'), related_name='content_type+')
    object_id = models.PositiveIntegerField(verbose_name=_('object id'))
    content_object = GenericForeignKey('content_type', 'object_id')
    relation_type = models.CharField(
        verbose_name=_('relation type'),
        max_length=200,
        blank=True,
        null=True,
        help_text=_("A generic text field to tag a relation, like 'leadphoto'."))

    objects = CategoryRelationManager()

    def __unicode__(self):
        return "CategoryRelation"

try:
    from south.db import db  # noqa, South is required for migrating. Need to check for it
    from django.db.models.signals import post_syncdb
    from wiki.plugins.categories.migration import migrate_app
    post_syncdb.connect(migrate_app)
except ImportError:
    pass
