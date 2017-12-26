# -*- coding: utf-8 -*-

from django.core import management
from django.core.management.base import CommandError
from django.test import TestCase


class TestMgmtCommands(TestCase):

    def test_add_category_fields(self):
        management.call_command('add_category_fields', verbosity=0)

    def test_add_category_fields_app(self):
        management.call_command('add_category_fields', 'flatpages', verbosity=0)

    def test_drop_category_field(self):
        management.call_command('drop_category_field', 'flatpages', 'flatpage', 'category', verbosity=0)

    def test_drop_category_field_error(self):
        self.assertRaises(CommandError, management.call_command, 'drop_category_field', verbosity=0)
