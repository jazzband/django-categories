from django.db import models

from categories.base import CategoryBase


class SimpleText(models.Model):
    """
    (SimpleText description)
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Simple Text'
        ordering = ('-created',)
        get_latest_by = 'updated'

    def __unicode__(self):
        return self.name

    # If using the get_absolute_url method, put the following line at the top of this file:
    from django.db.models import permalink

    @permalink
    def get_absolute_url(self):
        return ('simpletext_detail_view_name', [str(self.id)])


class SimpleCategory(CategoryBase):
    """A Test of catgorizing"""
    class Meta:
        verbose_name_plural = 'simple categories'


# mport categories

# ategories.register_fk(SimpleText, 'primary_category', {'related_name':'simpletext_primary_set'})
# ategories.register_m2m(SimpleText, 'cats', )
