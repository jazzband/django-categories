__version_info__ = {
    'major': 0,
    'minor': 5,
    'micro': 2,
    'releaselevel': 'final',
    'serial': 0
}

def get_version():
    vers = ["%(major)i.%(minor)i" % __version_info__, ]

    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final':
        vers.append('%(releaselevel)s%(serial)i' % __version_info__)
    return ''.join(vers)

__version__ = get_version()

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
except ImportError:
    pass
