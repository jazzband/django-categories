class Meta(CategoryBase.Meta):
    verbose_name_plural = 'categories'

class MPTTMeta:
    order_insertion_by = ('order', 'name')
