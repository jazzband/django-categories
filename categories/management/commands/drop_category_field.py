from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    """
    Alter one or more models' tables with the registered attributes
    """
    help = "Drop the given field from the given model's table"
    args = "appname modelname fieldname"
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
        
        from categories.migration import drop_field
        from categories import model_registry
        if len(args) != 3:
            print "You must specify an Application name, a Model name and a Field name"
        
        drop_field(*args)
