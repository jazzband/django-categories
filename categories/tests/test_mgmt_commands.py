from django.core import management
from django.core.management.base import CommandError
from django.db import connection
from django.test import TestCase


class TestMgmtCommands(TestCase):
    @classmethod
    def setUpClass(cls):
        connection.disable_constraint_checking()
        super(TestMgmtCommands, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestMgmtCommands, cls).tearDownClass()
        connection.enable_constraint_checking()

    def test_add_category_fields(self):
        management.call_command("add_category_fields", verbosity=0)

    def test_add_category_fields_app(self):
        management.call_command("add_category_fields", "flatpages", verbosity=0)

    def test_drop_category_field(self):
        management.call_command("drop_category_field", "flatpages", "flatpage", "category", verbosity=0)

    def test_drop_category_field_error(self):
        self.assertRaises(CommandError, management.call_command, "drop_category_field", verbosity=0)
