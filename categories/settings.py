from django.conf import settings
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
import collections

DEFAULT_SETTINGS = {
    'ALLOW_SLUG_CHANGE': False,
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
    if isinstance(DEFAULT_SETTINGS['SLUG_TRANSLITERATOR'], collections.Callable):
        pass
    elif isinstance(DEFAULT_SETTINGS['SLUG_TRANSLITERATOR'], str):
        from django.utils.importlib import import_module
        bits = DEFAULT_SETTINGS['SLUG_TRANSLITERATOR'].split(".")
        module = import_module(".".join(bits[:-1]))
        DEFAULT_SETTINGS['SLUG_TRANSLITERATOR'] = getattr(module, bits[-1])
    else:
        from django.core.exceptions import ImproperlyConfigured
        raise ImproperlyConfigured(_('%(transliterator) must be a callable or a string.') %
                                   {'transliterator': 'SLUG_TRANSLITERATOR'})
else:
    DEFAULT_SETTINGS['SLUG_TRANSLITERATOR'] = lambda x: x


# Add all the keys/values to the module's namespace
globals().update(DEFAULT_SETTINGS)

RELATIONS = [Q(app_label=al, model=m) for al, m in [x.split('.') for x in DEFAULT_SETTINGS['RELATION_MODELS']]]

# The field registry keeps track of the individual fields created.
#  {'app.model.field': Field(**extra_params)}
#  Useful for doing a schema migration
FIELD_REGISTRY = {}

# The model registry keeps track of which models have one or more fields
# registered.
# {'app': [model1, model2]}
# Useful for admin alteration
MODEL_REGISTRY = {}
