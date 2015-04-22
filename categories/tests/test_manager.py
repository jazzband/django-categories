# test active returns only active items
from django.test import TestCase
from categories.models import Category


class CategoryManagerTest(TestCase):
    fixtures = ['categories.json']

    def setUp(self):
        pass

    def testActive(self):
        """
        Should raise an exception.
        """
        all_count = Category.objects.all().count()
        self.assertEqual(Category.objects.active().count(), all_count)

        cat1 = Category.objects.get(name='Category 1')
        cat1.active = False
        cat1.save()

        active_count = all_count - cat1.get_descendants(True).count()
        self.assertEqual(Category.objects.active().count(), active_count)
