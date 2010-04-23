from django.conf import settings

ALLOW_SLUG_CHANGE = getattr(settings, 'CATEGORIES_ALLOW_SLUG_CHANGE', False)

CACHE_VIEW_LENGTH = getattr(settings, 'CATEGORIES_CACHE_VIEW_LENGTH', 3600)

from django.db.models import Q
DEFAULT_RELATION_MODELS = []
RELATION_MODELS = getattr(settings, 'CATEGORIES_RELATION_MODELS', DEFAULT_RELATION_MODELS) or []
RELATIONS = [Q(app_label=al, model=m) for al, m in [x.split('.') for x in RELATION_MODELS]]
