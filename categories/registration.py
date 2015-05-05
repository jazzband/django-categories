"""
These functions handle the adding of fields to other models
"""
from django.db.models import FieldDoesNotExist
import fields
from settings import FIELD_REGISTRY, MODEL_REGISTRY
from django.utils.translation import ugettext_lazy as _


def register_m2m(model, field_name='categories', extra_params={}):
    return _register(model, field_name, extra_params, fields.CategoryM2MField)


def register_fk(model, field_name='category', extra_params={}):
    return _register(model, field_name, extra_params, fields.CategoryFKField)


def _register(model, field_name, extra_params={}, field=fields.CategoryFKField):
    app_label = model._meta.app_label
    registry_name = ".".join((app_label, model.__name__, field_name)).lower()

    if registry_name in FIELD_REGISTRY:
        return  # raise AlreadyRegistered
    opts = model._meta
    try:
        opts.get_field(field_name)
    except FieldDoesNotExist:
        if app_label not in MODEL_REGISTRY:
            MODEL_REGISTRY[app_label] = []
        if model not in MODEL_REGISTRY[app_label]:
            MODEL_REGISTRY[app_label].append(model)
        FIELD_REGISTRY[registry_name] = field(**extra_params)
        FIELD_REGISTRY[registry_name].contribute_to_class(model, field_name)


def _process_registry(registry, call_func):
    """
    Given a dictionary, and a registration function, process the registry
    """
    from django.core.exceptions import ImproperlyConfigured
    from django.db.models.loading import get_model

    for key, value in registry.items():
        model = get_model(*key.split('.'))
        if model is None:
            raise ImproperlyConfigured(_('%(key)s is not a model') % {'key': key})
        if isinstance(value, (tuple, list)):
            for item in value:
                if isinstance(item, basestring):
                    call_func(model, item)
                elif isinstance(item, dict):
                    field_name = item.pop('name')
                    call_func(model, field_name, extra_params=item)
                else:
                    raise ImproperlyConfigured(_("%(settings)s doesn't recognize the value of %(key)s") %
                                               {'settings': 'CATEGORY_SETTINGS', 'key': key})
        elif isinstance(value, basestring):
            call_func(model, value)
        elif isinstance(value, dict):
            field_name = value.pop('name')
            call_func(model, field_name, extra_params=value)
        else:
            raise ImproperlyConfigured(_("%(settings)s doesn't recognize the value of %(key)s") %
                                       {'settings': 'CATEGORY_SETTINGS', 'key': key})
