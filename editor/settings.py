from django.conf import settings
import django

DJANGO10_COMPAT = django.VERSION[0] < 1 or (django.VERSION[0] == 1 and django.VERSION[1] < 1)

STATIC_URL = getattr(settings, 'STATIC_URL', settings.MEDIA_URL)
if STATIC_URL == None:
    STATIC_URL = settings.MEDIA_URL
MEDIA_PATH = getattr(settings, 'EDITOR_MEDIA_PATH', '%seditor/' % STATIC_URL)

TREE_INITIAL_STATE = getattr(settings, 'EDITOR_TREE_INITIAL_STATE', 'collapsed')