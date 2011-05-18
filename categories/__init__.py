__version_info__ = {
    'major': 0,
    'minor': 6,
    'micro': 0,
    'releaselevel': 'final',
    'serial': 1
}

def get_version():
    vers = ["%(major)i.%(minor)i" % __version_info__, ]

    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final':
        vers.append('%(releaselevel)s%(serial)i' % __version_info__)
    return ''.join(vers)

__version__ = get_version()

registry = {}

try:
    import fields
    
    from django.db.models import FieldDoesNotExist
    
    class AlreadyRegistered(Exception):
        """
        An attempt was made to register a model more than once.
        """
        pass
    
    registry = {}
    
    def register_m2m(model, field_name='categories', extra_params={}):
        return _register(model, field_name, extra_params, fields.CategoryM2MField)
    
    def register_fk(model, field_name='category', extra_params={}):
        return _register(model, field_name, extra_params, fields.CategoryFKField)
    
    def _register(model, field_name, extra_params={}, field=fields.CategoryFKField):
        registry_name = "%s.%s" % (model.__name__, field_name)
        
        if registry_name in registry:
            return #raise AlreadyRegistered
        registry[registry_name] = model
        opts = model._meta
        try:
            opts.get_field(field_name)
        except FieldDoesNotExist:
            field(**extra_params).contribute_to_class(model, field_name)
    
    from categories import settings
    from django.core.exceptions import ImproperlyConfigured
    from django.db.models import get_model
    
    for key, value in settings.FK_REGISTRY.items():
        model = get_model(*key.split('.'))
        if model is None:
            raise ImproperlyConfigured('%s is not a model' % key)
        if isinstance(value, (tuple, list)):
            for item in value:
                if isinstance(item, basestring):
                    register_fk(model, item)
                elif isinstance(item, dict):
                    field_name = item.pop('name')
                    register_fk(model, field_name, extra_params=item)
                else:
                    raise ImproperlyConfigured("CATEGORY_SETTINGS['FK_REGISTRY'] doesn't recognize the value of %s" % key)
        elif isinstance(value, basestring):
            register_fk(model, value)
        elif isinstance(item, dict):
            field_name = item.pop('name')
            register_fk(model, field_name, extra_params=item)
        else:
            raise ImproperlyConfigured("CATEGORY_SETTINGS['FK_REGISTRY'] doesn't recognize the value of %s" % key)
    for key, value in settings.M2M_REGISTRY.items():
        model = get_model(*key.split('.'))
        if model is None:
            raise ImproperlyConfigured('%s is not a model' % key)
        if isinstance(value, (tuple, list)):
            for item in value:
                if isinstance(item, basestring):
                    register_m2m(model, item)
                elif isinstance(item, dict):
                    field_name = item.pop('name')
                    register_m2m(model, field_name, extra_params=item)
                else:
                    raise ImproperlyConfigured("CATEGORY_SETTINGS['M2M_REGISTRY'] doesn't recognize the value of %s: %s" % (key, item))
        elif isinstance(value, basestring):
            register_m2m(model, value)
        elif isinstance(value, dict):
            field_name = value.pop('name')
            register_m2m(model, field_name, extra_params=value)
        else:
            raise ImproperlyConfigured("CATEGORY_SETTINGS['M2M_REGISTRY'] doesn't recognize the value of %s" % key)
    
except ImportError:
    pass
