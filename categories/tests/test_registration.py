# Test adding 1 fk string
# Test adding 1 fk dict
# test adding many-to-many
# test adding 1 fk, 1 m2m
import django
from django.test import TestCase

from categories.registration import _process_registry, registry


class CategoryRegistrationTest(TestCase):
    """
    Test various aspects of adding fields to a model.
    """

    def test_foreignkey_string(self):
        FK_REGISTRY = {
            'flatpages.flatpage': 'category'
        }
        _process_registry(FK_REGISTRY, registry.register_fk)
        from django.contrib.flatpages.models import FlatPage
        self.assertTrue('category' in [f.name for f in FlatPage()._meta.get_fields()])

    def test_foreignkey_dict(self):
        FK_REGISTRY = {
            'flatpages.flatpage': {'name': 'category'}
        }
        _process_registry(FK_REGISTRY, registry.register_fk)
        from django.contrib.flatpages.models import FlatPage
        self.assertTrue('category' in [f.name for f in FlatPage()._meta.get_fields()])

    def test_foreignkey_list(self):
        FK_REGISTRY = {
            'flatpages.flatpage': (
                {'name': 'category', 'related_name': 'cats'},
            )
        }
        _process_registry(FK_REGISTRY, registry.register_fk)
        from django.contrib.flatpages.models import FlatPage
        self.assertTrue('category' in [f.name for f in FlatPage()._meta.get_fields()])

    if django.VERSION[1] >= 7:
        def test_new_foreignkey_string(self):
            registry.register_model('flatpages', 'flatpage', 'ForeignKey', 'category')
            from django.contrib.flatpages.models import FlatPage
            self.assertTrue('category' in [f.name for f in FlatPage()._meta.get_fields()])


class Categorym2mTest(TestCase):
    def test_m2m_string(self):
        M2M_REGISTRY = {
            'flatpages.flatpage': 'categories'
        }
        _process_registry(M2M_REGISTRY, registry.register_m2m)
        from django.contrib.flatpages.models import FlatPage
        self.assertTrue('category' in [f.name for f in FlatPage()._meta.get_fields()])
