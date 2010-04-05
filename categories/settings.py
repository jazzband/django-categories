from django.conf import settings

ALLOW_SLUG_CHANGE = getattr(settings, 'CATEGORIES_ALLOW_SLUG_CHANGE', False)

CACHE_VIEW_LENGTH = getattr(settings, 'CATEGORIES_CACHE_VIEW_LENGTH', 3600)