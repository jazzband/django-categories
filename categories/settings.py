import warnings

from django.conf import settings
from django.db.models import Q

CATEGORIES_SETTINGS = {
    'ALLOW_SLUG_CHANGE': False,
    'CACHE_VIEW_LENGTH': 0,
    'RELATION_MODELS': [],
    'M2M_REGISTRY': [],
    'FK_REGISTRY': []
}

CATEGORIES_SETTINGS.update(getattr(settings, 'CATEGORIES_SETTINGS', {}))

if hasattr(settings, 'CATEGORIES_ALLOW_SLUG_CHANGE'):
    warnings.warn(
        "settings.CATEGORIES_ALLOW_SLUG_CHANGE is deprecated; use settings.CATEGORIES_SETTINGS instead.",
        DeprecationWarning
    )
    ALLOW_SLUG_CHANGE = getattr(settings, 'CATEGORIES_ALLOW_SLUG_CHANGE')
else:
    ALLOW_SLUG_CHANGE = CATEGORIES_SETTINGS['ALLOW_SLUG_CHANGE']

if hasattr(settings, 'CATEGORIES_CACHE_VIEW_LENGTH'):
    warnings.warn(
        "settings.CATEGORIES_CACHE_VIEW_LENGTH is deprecated; use settings.CATEGORIES_SETTINGS instead.",
        DeprecationWarning
    )
    CACHE_VIEW_LENGTH = getattr(settings, 'CATEGORIES_CACHE_VIEW_LENGTH')
else:
    CACHE_VIEW_LENGTH = CATEGORIES_SETTINGS['CACHE_VIEW_LENGTH']

if hasattr(settings, 'CATEGORIES_RELATION_MODELS'):
    warnings.warn(
        "settings.CATEGORIES_RELATION_MODELS is deprecated; use settings.CATEGORIES_SETTINGS instead.",
        DeprecationWarning
    )
    RELATION_MODELS = getattr(settings, 'CATEGORIES_RELATION_MODELS')
else:
    RELATION_MODELS = CATEGORIES_SETTINGS['RELATION_MODELS']

RELATIONS = [Q(app_label=al, model=m) for al, m in [x.split('.') for x in RELATION_MODELS]]

# For assigning a thumbnail to a category
THUMBNAIL_UPLOAD_PATH = getattr(settings, 'CATEGORIES_THUMBNAIL_UPLOAD_PATH', 'uploads/categories/thumbnails')
