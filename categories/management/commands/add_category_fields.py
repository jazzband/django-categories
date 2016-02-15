from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Alter one or more models' tables with the registered attributes
    """
    help = "Alter the tables for all registered models, or just specified models"
    args = "[appname ...]"
    can_import_settings = True
    requires_model_validation = False

    def handle(self, *args, **options):
        """
        Alter the tables
        """

        from categories.migration import migrate_app
        from categories.settings import MODEL_REGISTRY
        if args:
            for app in args:
                migrate_app(None, app)
        else:
            for app in MODEL_REGISTRY:
                migrate_app(None, app)
