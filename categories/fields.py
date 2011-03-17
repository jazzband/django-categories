from django.db.models import ForeignKey, ManyToManyField

from categories.models import Category



class CategoryM2MField(ManyToManyField):
    def __init__(self, **kwargs):
        if 'to' in kwargs:
            kwargs.pop('to')
        super(CategoryM2MField, self).__init__(to=Category, **kwargs)


class CategoryFKField(ForeignKey):
    def __init__(self, **kwargs):
        if 'to' in kwargs:
            kwargs.pop('to')
        super(CategoryFKField, self).__init__(to=Category, **kwargs)
