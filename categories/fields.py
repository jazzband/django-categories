from django.db.models import ForeignKey, ManyToManyField

class CategoryM2MField(ManyToManyField):
    def __init__(self, **kwargs):
        from categories.models import Category
        super(CategoryM2MField, self).__init__(to=Category, **kwargs)


class CategoryFKField(ForeignKey):
    def __init__(self, **kwargs):
        from categories.models import Category
        super(CategoryFKField, self).__init__(to=Category, **kwargs)