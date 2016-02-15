# test spaces in hierarchy
# test tabs in hierarchy
# test mixed
import os

from django.conf import settings
from django.test import TestCase, override_settings
from categories.models import Category
from categories.management.commands.import_categories import Command
from django.core.management.base import CommandError


@override_settings(INSTALLED_APPS=(app for app in settings.INSTALLED_APPS if app != 'django.contrib.flatpages'))
class CategoryImportTest(TestCase):
    def setUp(self):
        pass

    def _import_file(self, filename):
        root_cats = ['Category 1', 'Category 2', 'Category 3']
        testfile = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fixtures', filename))
        cmd = Command()
        cmd.execute(testfile)
        roots = Category.tree.root_nodes()

        self.assertEqual(len(roots), 3)
        for item in roots:
            assert item.name in root_cats

        cat2 = Category.objects.get(name='Category 2')
        cat21 = cat2.children.all()[0]
        self.assertEqual(cat21.name, 'Category 2-1')
        cat211 = cat21.children.all()[0]
        self.assertEqual(cat211.name, 'Category 2-1-1')

    def testImportSpaceDelimited(self):
        Category.objects.all().delete()
        self._import_file('test_category_spaces.txt')

        items = Category.objects.all()

        self.assertEqual(items[0].name, 'Category 1')
        self.assertEqual(items[1].name, 'Category 1-1')
        self.assertEqual(items[2].name, 'Category 1-2')

    def testImportTabDelimited(self):
        Category.objects.all().delete()
        self._import_file('test_category_tabs.txt')

        items = Category.objects.all()

        self.assertEqual(items[0].name, 'Category 1')
        self.assertEqual(items[1].name, 'Category 1-1')
        self.assertEqual(items[2].name, 'Category 1-2')

    def testMixingTabsSpaces(self):
        """
        Should raise an exception.
        """
        string1 = ["cat1", "    cat1-1", "\tcat1-2-FAIL!", ""]
        string2 = ["cat1", "\tcat1-1", "    cat1-2-FAIL!", ""]
        cmd = Command()

        # raise Exception
        self.assertRaises(CommandError, cmd.parse_lines, string1)
        self.assertRaises(CommandError, cmd.parse_lines, string2)
