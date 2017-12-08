from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core.files.storage import get_storage_class
from django.core.urlresolvers import reverse
from django.db import models
from django.db import transaction
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext_lazy as _

from categories.base import CategoryBase
from categories.settings import (RELATION_MODELS, RELATIONS, THUMBNAIL_UPLOAD_PATH,
                        THUMBNAIL_STORAGE)

STORAGE = get_storage_class(THUMBNAIL_STORAGE)

@transaction.commit_manually
def flush_transaction():
    transaction.commit()

class Category(CategoryBase):
    thumbnail = models.FileField(
        upload_to=THUMBNAIL_UPLOAD_PATH,
        null=True, blank=True,
        storage=STORAGE(),)
    thumbnail_width = models.IntegerField(blank=True, null=True)
    thumbnail_height = models.IntegerField(blank=True, null=True)
    mobile_thumbnail = models.FileField(
        upload_to=THUMBNAIL_UPLOAD_PATH,
        null=True, blank=True,
        storage=STORAGE(),)
    mobile_thumbnail_width = models.IntegerField(blank=True, null=True)
    mobile_thumbnail_height = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(default=0, null=True)
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
    is_blog = models.BooleanField(default=False, blank=False, null=False)
    show_converser_ad = models.BooleanField("Show a converser ad?", default=False,
        help_text="Select to enable a converser ad for the category page. A 600x300 converser ad unit must be " \
                  "active in Dart.")

    is_sponsored = models.BooleanField(default=False, blank=False, null=False,
                                       help_text="This field is automatically marked as true if there are one or more sponsors assigned to this category. " \
                                                 "It may also be manually marked true if there are no assigned sponsors.")

    sponsorships = models.ManyToManyField(
        "post_manager.ContentSponsorship",
        through="categories.CategorySponsor",
        help_text="Adding a sponsor will automatically mark 'Is sponsored' as true. " \
                  "Removing a sponsor or all sponsors will not affect the value of 'Is sponsored'.")

    @property
    def display_converser(self):
        """
        This method flushes the database cache to get the current value of the "show_converser_ad" field
        """
        if not hasattr(self, '_uncached_show_converser_ad'):
            flush_transaction()
            uncached_show_converser_ad_list = Category.objects.values('show_converser_ad').filter(id=self.id)
            if len(uncached_show_converser_ad_list) > 0:
                if uncached_show_converser_ad_list[0]['show_converser_ad']:
                    self._uncached_show_converser_ad = True
                else:
                    self._uncached_show_converser_ad = False
        return self._uncached_show_converser_ad

    @property
    def short_title(self):
        return self.name

    def get_absolute_url(self):
        """Return a path"""
        if self.alternate_url:
            return self.alternate_url
        prefix = reverse('categories_tree_list')
        ancestors = list(self.get_ancestors()) + [self, ]
        # remove top-level category from display
        if len(ancestors) > 0:
            del ancestors[0]
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

    class Meta(CategoryBase.Meta):
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    class MPTTMeta:
        order_insertion_by = ('name')


if RELATIONS:
    CATEGORY_RELATION_LIMITS = reduce(lambda x, y: x | y, RELATIONS)
else:
    CATEGORY_RELATION_LIMITS = []


class CategoryRelationManager(models.Manager):
    def get_content_type(self, content_type):
        """
        Get all the items of the given content type related to this item.
        """
        qs = self.get_query_set()
        return qs.filter(content_type__name=content_type)

    def get_relation_type(self, relation_type):
        """
        Get all the items of the given relationship type related to this item.
        """
        qs = self.get_query_set()
        return qs.filter(relation_type=relation_type)


class CategoryRelation(models.Model):
    """Related category item"""
    category = models.ForeignKey(Category, verbose_name=_('category'))
    content_type = models.ForeignKey(
        ContentType, limit_choices_to=CATEGORY_RELATION_LIMITS, verbose_name=_('content type'))
    object_id = models.PositiveIntegerField(verbose_name=_('object id'))
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    relation_type = models.CharField(verbose_name=_('relation type'),
        max_length="200",
        blank=True,
        null=True,
        help_text=_("A generic text field to tag a relation, like 'leadphoto'."))

    objects = CategoryRelationManager()

    def __unicode__(self):
        return u"CategoryRelation"

class CategorySponsor(models.Model):
    category = models.ForeignKey(Category)
    sponsorship = models.ForeignKey("post_manager.ContentSponsorship", verbose_name=u"sponsor")
    url = models.URLField(u"URL", null=True, blank=True)
    order = models.IntegerField()

    class Meta:
        verbose_name = u"sponsor"
        db_table = "post_manager_categorysponsor"
