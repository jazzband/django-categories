import fields
import models

from django.db.models import FieldDoesNotExist

class AlreadyRegistered(Exception):
    """
    An attempt was made to register a model more than once.
    """
    pass

registry = []

def register_m2m(model, field_name='categories', extra_params={}):
    return _register(model, field_name, extra_params, fields.CategoryM2MField)
    
def register_fk(model, field_name='category', extra_params={}):
    return _register(model, field_name, extra_params, fields.CategoryFKField)
    
def _register(model, field_name, extra_params={}, field=fields.CategoryFKField):
    if model in registry:
        raise AlreadyRegistered('The model %s has already been registered.' % model.__name__)
    registry.append(model)
    
    opts = model._meta
    try:
        opts.get_field(field_name)
    except FieldDoesNotExist:
        field(**extra_params).contribute_to_class(model, field_name)