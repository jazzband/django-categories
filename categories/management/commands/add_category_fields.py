from django.core.management.base import BaseCommand, CommandError

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
        try:
            from south.db import db
        except ImportError:
            raise ImproperlyConfigured("South must be installed for this command to work")
        
        from categories.migration import migrate_app
        from categories import model_registry
        if args:
            for app in args:
                migrate_app(app)
        else:
            for app in model_registry:
                migrate_app(app)
