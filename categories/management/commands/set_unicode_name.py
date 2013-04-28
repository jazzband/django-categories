from django.core.management.base import BaseCommand, CommandError
from categories.models import Category


class Command(BaseCommand):
    """
    Alter one or more models' tables with the registered attributes
    """
    def handle(self, *args, **options):
        categories = Category.objects.filter(unicode_name=None)
        for category in categories:
            print "%s=[%s]" % (category.name, category.generate_unicode_name(),)
            category.unicode_name = category.generate_unicode_name()
            category.save()