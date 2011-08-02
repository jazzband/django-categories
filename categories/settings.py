import warnings

from django.conf import settings
from django.db.models import Q

DEFAULT_SETTINGS = {
    'ALLOW_SLUG_CHANGE': False,
    'CACHE_VIEW_LENGTH': 0,
    'RELATION_MODELS': [],
    'M2M_REGISTRY': {},
    'FK_REGISTRY': {},
    'THUMBNAIL_UPLOAD_PATH': 'uploads/categories/thumbnails',
    'THUMBNAIL_STORAGE': settings.DEFAULT_FILE_STORAGE,
    'JAVASCRIPT_URL': getattr(settings, 'STATIC_URL', settings.MEDIA_URL) + 'js/',
}

DEFAULT_SETTINGS.update(getattr(settings, 'CATEGORIES_SETTINGS', {}))

ERR_MSG = "settings.%s is deprecated; use settings.CATEGORIES_SETTINGS instead."

if hasattr(settings, 'CATEGORIES_ALLOW_SLUG_CHANGE'):
    warnings.warn(ERR_MSG % 'CATEGORIES_ALLOW_SLUG_CHANGE', DeprecationWarning)
    DEFAULT_SETTINGS["ALLOW_SLUG_CHANGE"] = getattr(settings, 'CATEGORIES_ALLOW_SLUG_CHANGE')

if hasattr(settings, 'CATEGORIES_CACHE_VIEW_LENGTH'):
    warnings.warn(ERR_MSG % "CATEGORIES_CACHE_VIEW_LENGTH", DeprecationWarning)
    DEFAULT_SETTINGS["CACHE_VIEW_LENGTH"] = getattr(settings, 'CATEGORIES_CACHE_VIEW_LENGTH')

if hasattr(settings, 'CATEGORIES_THUMBNAIL_UPLOAD_PATH'):
    warnings.warn(ERR_MSG % "CATEGORIES_THUMBNAIL_UPLOAD_PATH", DeprecationWarning)
    DEFAULT_SETTINGS["THUMBNAIL_UPLOAD_PATH"] = getattr(settings, 'CATEGORIES_THUMBNAIL_UPLOAD_PATH')

if hasattr(settings, 'CATEGORIES_RELATION_MODELS'):
    warnings.warn(ERR_MSG % "CATEGORIES_RELATION_MODELS", DeprecationWarning)
    DEFAULT_SETTINGS["RELATION_MODELS"] = getattr(settings, 'CATEGORIES_RELATION_MODELS')

# Add all the keys/values to the module's namespace
globals().update(DEFAULT_SETTINGS)

RELATIONS = [Q(app_label=al, model=m) for al, m in [x.split('.') for x in RELATION_MODELS]]
