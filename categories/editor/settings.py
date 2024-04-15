"""Settings management for the editor."""

from django.conf import settings

STATIC_URL = getattr(settings, "STATIC_URL", settings.MEDIA_URL)
if STATIC_URL is None:
    STATIC_URL = settings.MEDIA_URL
MEDIA_PATH = getattr(settings, "EDITOR_MEDIA_PATH", "%seditor/" % STATIC_URL)

TREE_INITIAL_STATE = getattr(settings, "EDITOR_TREE_INITIAL_STATE", "collapsed")

IS_GRAPPELLI_INSTALLED = "grappelli" in settings.INSTALLED_APPS
