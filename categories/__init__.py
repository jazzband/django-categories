import fields
import models

from django.db.models import FieldDoesNotExist

def register_m2m(model, field_name, extra_params={}):
    return _register(model, field_name, extra_params, fields.CategoryM2MField)
    

def register_fk(model, field_name, extra_params={}):
    return _register(model, field_name, extra_params, fields.CategoryFKField)
    
def _register(model, field_name='category', extra_params={}, field=fields.CategoryFKField):
    opts = model._meta
    try:
        opts.get_field(field_name)
    except FieldDoesNotExist:
        field(**extra_params).contribute_to_class(model, field_name)