from django.conf import settings
import django

DJANGO10_COMPAT = django.VERSION[0] < 1 or (django.VERSION[0] == 1 and django.VERSION[1] < 1)

MEDIA_PATH = getattr(settings, 'EDITOR_MEDIA_PATH', '/media/editor/')

# Link to google APIs instead of using local copy of JS libraries
MEDIA_HOTLINKING = getattr(settings, 'EDITOR_MEDIA_HOTLINKING', False)
