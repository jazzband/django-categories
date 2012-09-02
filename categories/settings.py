import warnings

from django.conf import settings
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

DEFAULT_SETTINGS = {
    'ALLOW_SLUG_CHANGE': False,
    'CACHE_VIEW_LENGTH': 600,
    'RELATION_MODELS': [],
    'M2M_REGISTRY': {},
    'FK_REGISTRY': {},
    'THUMBNAIL_UPLOAD_PATH': 'uploads/categories/thumbnails',
    'THUMBNAIL_STORAGE': settings.DEFAULT_FILE_STORAGE,
    'JAVASCRIPT_URL': getattr(settings, 'STATIC_URL', settings.MEDIA_URL) + 'js/',
    'SLUG_TRANSLITERATOR': '',
    'REGISTER_ADMIN': True,
    'RELATION_MODELS': [],
}

DEFAULT_SETTINGS.update(getattr(settings, 'CATEGORIES_SETTINGS', {}))

if DEFAULT_SETTINGS['SLUG_TRANSLITERATOR']:
    if callable(DEFAULT_SETTINGS['SLUG_TRANSLITERATOR']):
        pass
    elif isinstance(DEFAULT_SETTINGS['SLUG_TRANSLITERATOR'], basestring):
        from django.utils.importlib import import_module
        bits = DEFAULT_SETTINGS['SLUG_TRANSLITERATOR'].split(".")
        module = import_module(".".join(bits[:-1]))
        DEFAULT_SETTINGS['SLUG_TRANSLITERATOR'] = getattr(module, bits[-1])
    else:
        from django.core.exceptions import ImproperlyConfigured
        raise ImproperlyConfigured(_('%(transliterator) must be a callable or a string.') %
                                   {'transliterator' : 'SLUG_TRANSLITERATOR'})
else:
    DEFAULT_SETTINGS['SLUG_TRANSLITERATOR'] = lambda x: x

def warn_deprecated(deprecated_setting, replacement):
    warnings.warn(_('%(deprecated_setting) is deprecated; use %(replacement)s instead.') %
                  {'deprecated_setting' : deprecated_setting, 'replacement' : replacement}, DeprecationWarning)

if hasattr(settings, 'CATEGORIES_ALLOW_SLUG_CHANGE'):
    warn_deprecated('settings.CATEGORIES_ALLOW_SLUG_CHANGE', 'settings.CATEGORIES_SETTINGS')
    DEFAULT_SETTINGS["ALLOW_SLUG_CHANGE"] = getattr(settings, 'CATEGORIES_ALLOW_SLUG_CHANGE')

if hasattr(settings, 'CATEGORIES_CACHE_VIEW_LENGTH'):
    warn_deprecated('settings.CATEGORIES_CACHE_VIEW_LENGTH', 'settings.CATEGORIES_SETTINGS')
    DEFAULT_SETTINGS["CACHE_VIEW_LENGTH"] = getattr(settings, 'CATEGORIES_CACHE_VIEW_LENGTH')

if hasattr(settings, 'CATEGORIES_THUMBNAIL_UPLOAD_PATH'):
    warn_deprecated('settings.CATEGORIES_THUMBNAIL_UPLOAD_PATH', 'settings.CATEGORIES_SETTINGS')
    DEFAULT_SETTINGS["THUMBNAIL_UPLOAD_PATH"] = getattr(settings, 'CATEGORIES_THUMBNAIL_UPLOAD_PATH')

if hasattr(settings, 'CATEGORIES_RELATION_MODELS'):
    warn_deprecated('settings.CATEGORIES_RELATION_MODELS', 'settings.CATEGORIES_SETTINGS')
    DEFAULT_SETTINGS["RELATION_MODELS"] = getattr(settings, 'CATEGORIES_RELATION_MODELS')

# Add all the keys/values to the module's namespace
globals().update(DEFAULT_SETTINGS)

RELATIONS = [Q(app_label=al, model=m) for al, m in [x.split('.') for x in RELATION_MODELS]]

# The field registry keeps track of the individual fields created.
#  {'app.model.field': Field(**extra_params)}
#  Useful for doing a schema migration
FIELD_REGISTRY = {}

# The model registry keeps track of which models have one or more fields
# registered.
# {'app': [model1, model2]}
# Useful for admin alteration
MODEL_REGISTRY = {}
