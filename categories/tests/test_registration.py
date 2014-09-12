# Test adding 1 fk string
# Test adding 1 fk dict
# test adding many-to-many
# test adding 1 fk, 1 m2m

from django.test import TestCase

from categories.registration import (_process_registry, register_fk,
                                        register_m2m)


class CategoryRegistrationTest(TestCase):
    """
    Test various aspects of adding fields to a model.
    """

    def test_foreignkey_string(self):
        FK_REGISTRY = {
            'flatpages.flatpage': 'category'
        }
        _process_registry(FK_REGISTRY, register_fk)
        from django.contrib.flatpages.models import FlatPage
        self.assertTrue('category' in FlatPage()._meta.get_all_field_names())

    def test_foreignkey_dict(self):
        FK_REGISTRY = {
            'flatpages.flatpage': {'name': 'category'}
        }
        _process_registry(FK_REGISTRY, register_fk)
        from django.contrib.flatpages.models import FlatPage
        self.assertTrue('category' in FlatPage()._meta.get_all_field_names())

    def test_foreignkey_list(self):
        FK_REGISTRY = {
            'flatpages.flatpage': (
                {'name': 'category', 'related_name': 'cats'},
            )
        }
        _process_registry(FK_REGISTRY, register_fk)
        from django.contrib.flatpages.models import FlatPage
        self.assertTrue('category' in FlatPage()._meta.get_all_field_names())


# class Categorym2mTest(TestCase):
#     def test_m2m_string(self):
#         M2M_REGISTRY = {
#             'flatpages.flatpage': 'categories'
#         }
#         _process_registry(M2M_REGISTRY, register_m2m)
#         from django.contrib.flatpages.models import FlatPage
#         self.assertTrue('category' in FlatPage()._meta.get_all_field_names())
