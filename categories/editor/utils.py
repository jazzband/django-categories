"""
Provides compatibility with Django 1.8.
"""
from django.contrib.admin.utils import display_for_field as _display_for_field


def display_for_field(value, field, empty_value_display=None):
    """Compatility for displaying a field in Django 1.8."""
    try:
        return _display_for_field(value, field, empty_value_display)
    except TypeError:
        return _display_for_field(value, field)
