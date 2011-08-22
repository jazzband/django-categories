# test active returns only active items
import unittest, os
from categories.models import Category
from categories.management.commands.import_categories import Command
from django.core.management.base import CommandError

class CategoryManagerTest(unittest.TestCase):
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
