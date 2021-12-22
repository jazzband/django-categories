"""Custom category fields for other models."""
from django.db.models import ForeignKey, ManyToManyField


class CategoryM2MField(ManyToManyField):
    """A many to many field to a Category model."""

    def __init__(self, **kwargs):
        from .models import Category

        if "to" in kwargs:
            kwargs.pop("to")
        super(CategoryM2MField, self).__init__(to=Category, **kwargs)


class CategoryFKField(ForeignKey):
    """A foreign key to the Category model."""

    def __init__(self, **kwargs):
        from .models import Category

        if "to" in kwargs:
            kwargs.pop("to")
        super(CategoryFKField, self).__init__(to=Category, **kwargs)
