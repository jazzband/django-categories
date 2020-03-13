import sys


if (sys.version_info >= (3, 0)):
    from django_test_migrations.contrib.unittest_case import MigratorTestCase

    class TestMigrations(MigratorTestCase):

        migrate_from = ('categories', '0003_auto_20200306_1050')
        migrate_to = ('categories', '0004_unique_category_slug')

        def prepare(self):
            Category = self.old_state.apps.get_model('categories', 'Category')
            Category.tree.create(slug='foo', lft=0, rght=0, tree_id=0, level=0)
            Category.tree.create(slug='foo', lft=0, rght=0, tree_id=0, level=0)
            Category.tree.create(slug='foo', lft=0, rght=0, tree_id=0, level=0)
            for i in range(1, 12):
                Category.tree.create(slug='bar', lft=0, rght=0, tree_id=0, level=0)
            Category.tree.create(slug='baz', lft=0, rght=0, tree_id=0, level=0)
            assert Category.tree.count() == 15

        def test_unique_slug_migration(self):
            Category = self.new_state.apps.get_model('categories', 'Category')

            self.assertListEqual(
                list(Category.tree.values_list('slug', flat=True)),
                [
                    'foo',
                    'foo_1',
                    'foo_2',
                    'bar',
                    'bar_01',
                    'bar_02',
                    'bar_03',
                    'bar_04',
                    'bar_05',
                    'bar_06',
                    'bar_07',
                    'bar_08',
                    'bar_09',
                    'bar_10',
                    'baz',
                ],
            )
