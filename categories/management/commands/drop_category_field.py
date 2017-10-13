from django.core.management.base import BaseCommand
from django.core.management.base import CommandError


class Command(BaseCommand):
    """
    Alter one or more models' tables with the registered attributes
    """
    help = "Drop the given field from the given model's table"
    args = "appname modelname fieldname"
    can_import_settings = True
    requires_system_checks = False

    def add_arguments(self, parser):
        parser.add_argument('app_name')
        parser.add_argument('model_name')
        parser.add_argument('field_name')

    def handle(self, *args, **options):
        """
        Alter the tables
        """
        from categories.migration import drop_field
        if 'app_name' not in options or 'model_name' not in options or 'field_name' not in options:
            raise CommandError("You must specify an Application name, a Model name and a Field name")

        drop_field(options['app_name'], options['model_name'], options['field_name'])
