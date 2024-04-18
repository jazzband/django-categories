"""This module contains utility functions that are used across the project."""

from django.utils.text import slugify as django_slugify


def slugify(text):
    """Slugify a string. This function is a wrapper to unify the slugify function across the project."""
    return django_slugify(text, allow_unicode=True)
