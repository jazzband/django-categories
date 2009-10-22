from django.conf import settings

ALLOW_SLUG_CHANGE = getattr(settings, 'CATEGORIES_ALLOW_SLUG_CHANGE', False)