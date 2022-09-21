"""The add_category_fields command."""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Alter one or more models' tables with the registered attributes.
    """

    help = "Alter the tables for all registered models, or just specified models"
    args = "[appname ...]"
    can_import_settings = True
    requires_system_checks = []

    def add_arguments(self, parser):
        """Add app_names argument to the command."""
        parser.add_argument("app_names", nargs="*")

    def handle(self, *args, **options):
        """
        Alter the tables.
        """
        from categories.migration import migrate_app
        from categories.settings import MODEL_REGISTRY

        if options["app_names"]:
            for app in options["app_names"]:
                migrate_app(None, app)
        else:
            for app in MODEL_REGISTRY:
                migrate_app(None, app)
