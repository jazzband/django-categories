"""
These functions handle the adding of fields to other models
"""
from django.db.models import FieldDoesNotExist, ForeignKey, ManyToManyField
from . import fields
# from settings import self._field_registry, self._model_registry
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ImproperlyConfigured


FIELD_TYPES = {
    'ForeignKey': ForeignKey,
    'ManyToManyField': ManyToManyField,
}


class Registry(object):
    def __init__(self):
        self._field_registry = {}
        self._model_registry = {}

    def register_model(self, app, model_name, field_type, field_definitions):
        """
        Process for Django 1.7 +
        app: app name/label
        model_name: name of the model
        field_definitions: a string, tuple or list of field configurations
        field_type: either 'ForeignKey' or 'ManyToManyField'
        """
        from django.apps import apps
        import collections

        app_label = app

        if isinstance(field_definitions, str):
            field_definitions = [field_definitions]
        elif not isinstance(field_definitions, collections.Iterable):
            raise ImproperlyConfigured(_('Field configuration for %(app)s should be a string or iterable') % {'app': app})

        if field_type not in ('ForeignKey', 'ManyToManyField'):
            raise ImproperlyConfigured(_('`field_type` must be either `"ForeignKey"` or `"ManyToManyField"`.'))

        try:
            if not hasattr(model_name, "_meta"):
                app_config = apps.get_app_config(app)
                app_label = app_config.label
                model = app_config.get_model(model_name)
            else:
                model = model_name
                model_name = model._meta.model_name
            opts = model._meta
            if app_label not in self._model_registry:
                self._model_registry[app_label] = []
            if model not in self._model_registry[app_label]:
                self._model_registry[app_label].append(model)
        except LookupError:
            raise ImproperlyConfigured('Model "%(model)s" doesn\'t exist in app "%(app)s".' % {'model': model_name, 'app': app})

        if not isinstance(field_definitions, (tuple, list)):
            field_definitions = [field_definitions]

        for fld in field_definitions:
            extra_params = {'to': 'categories.Category', 'blank': True}
            if field_type != 'ManyToManyField':
                extra_params['null'] = True
            if isinstance(fld, str):
                field_name = fld
            elif isinstance(fld, dict):
                if 'name' in fld:
                    field_name = fld.pop('name')
                else:
                    continue
                extra_params.update(fld)
            else:
                raise ImproperlyConfigured(
                    _("%(settings)s doesn't recognize the value of %(app)s.%(model)s") % {
                        'settings': 'CATEGORY_SETTINGS',
                        'app': app,
                        'model': model_name})
            registry_name = ".".join([app_label, model_name.lower(), field_name])
            if registry_name in self._field_registry:
                continue

            try:
                opts.get_field(field_name)
            except FieldDoesNotExist:
                self._field_registry[registry_name] = FIELD_TYPES[field_type](**extra_params)
                self._field_registry[registry_name].contribute_to_class(model, field_name)

    def register_m2m(self, model, field_name='categories', extra_params={}):
        return self._register(model, field_name, extra_params, fields.CategoryM2MField)

    def register_fk(self, model, field_name='category', extra_params={}):
        return self._register(model, field_name, extra_params, fields.CategoryFKField)

    def _register(self, model, field_name, extra_params={}, field=fields.CategoryFKField):
        app_label = model._meta.app_label
        registry_name = ".".join((app_label, model.__name__, field_name)).lower()

        if registry_name in self._field_registry:
            return  # raise AlreadyRegistered
        opts = model._meta
        try:
            opts.get_field(field_name)
        except FieldDoesNotExist:
            if app_label not in self._model_registry:
                self._model_registry[app_label] = []
            if model not in self._model_registry[app_label]:
                self._model_registry[app_label].append(model)
            self._field_registry[registry_name] = field(**extra_params)
            self._field_registry[registry_name].contribute_to_class(model, field_name)

registry = Registry()


def _process_registry(registry, call_func):
    """
    Given a dictionary, and a registration function, process the registry
    """
    from django.core.exceptions import ImproperlyConfigured
    from django.apps import apps

    for key, value in list(registry.items()):
        model = apps.get_model(*key.split('.'))
        if model is None:
            raise ImproperlyConfigured(_('%(key)s is not a model') % {'key': key})
        if isinstance(value, (tuple, list)):
            for item in value:
                if isinstance(item, str):
                    call_func(model, item)
                elif isinstance(item, dict):
                    field_name = item.pop('name')
                    call_func(model, field_name, extra_params=item)
                else:
                    raise ImproperlyConfigured(_("%(settings)s doesn't recognize the value of %(key)s") %
                                               {'settings': 'CATEGORY_SETTINGS', 'key': key})
        elif isinstance(value, str):
            call_func(model, value)
        elif isinstance(value, dict):
            field_name = value.pop('name')
            call_func(model, field_name, extra_params=value)
        else:
            raise ImproperlyConfigured(_("%(settings)s doesn't recognize the value of %(key)s") %
                                       {'settings': 'CATEGORY_SETTINGS', 'key': key})
