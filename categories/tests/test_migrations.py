import sys

if sys.version_info >= (3, 0):
    from django_test_migrations.contrib.unittest_case import MigratorTestCase

    class TestMigrations(MigratorTestCase):
        migrate_from = ("categories", "0004_auto_20200517_1832")
        migrate_to = ("categories", "0005_unique_category_slug")

        def prepare(self):
            Category = self.old_state.apps.get_model("categories", "Category")
            Category.tree.create(slug="foo", lft=0, rght=0, tree_id=0, level=0)
            Category.tree.create(slug="foo", lft=0, rght=0, tree_id=0, level=0)
            Category.tree.create(slug="foo", lft=0, rght=0, tree_id=0, level=0)
            for i in range(1, 12):
                Category.tree.create(slug="bar", lft=0, rght=0, tree_id=0, level=0)
            Category.tree.create(slug="baz", lft=0, rght=0, tree_id=0, level=0)
            assert Category.tree.count() == 15

        def test_unique_slug_migration(self):
            Category = self.new_state.apps.get_model("categories", "Category")

            self.assertListEqual(
                list(Category.tree.values_list("slug", flat=True)),
                [
                    "foo",
                    "foo-1",
                    "foo-2",
                    "bar",
                    "bar-01",
                    "bar-02",
                    "bar-03",
                    "bar-04",
                    "bar-05",
                    "bar-06",
                    "bar-07",
                    "bar-08",
                    "bar-09",
                    "bar-10",
                    "baz",
                ],
            )
