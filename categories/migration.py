# -*- coding: utf-8 -*-


from django.db import connection, transaction
from django.apps import apps
from django.db.utils import ProgrammingError


def table_exists(table_name):
    """
    Check if a table exists in the database
    """
    pass


def field_exists(app_name, model_name, field_name):
    """
    Does the FK or M2M table exist in the database already?
    """
    model = apps.get_model(app_name, model_name)
    table_name = model._meta.db_table
    cursor = connection.cursor()
    field_info = connection.introspection.get_table_description(cursor, table_name)
    field_names = [f.name for f in field_info]
    return field_name in field_names


def drop_field(app_name, model_name, field_name):
    """
    Drop the given field from the app's model
    """
    app_config = apps.get_app_config(app_name)
    model = app_config.get_model(model_name)
    field = model._meta.get_field(field_name)
    with connection.schema_editor() as schema_editor:
        schema_editor.remove_field(model, field)


def migrate_app(sender, *args, **kwargs):
    """
    Migrate all models of this app registered
    """
    from .registration import registry
    if 'app_config' not in kwargs:
        return
    app_config = kwargs['app_config']

    app_name = app_config.label

    fields = [fld for fld in list(registry._field_registry.keys()) if fld.startswith(app_name)]

    sid = transaction.savepoint()
    for fld in fields:
        model_name, field_name = fld.split('.')[1:]
        if field_exists(app_name, model_name, field_name):
            continue
        model = app_config.get_model(model_name)
        try:
            with connection.schema_editor() as schema_editor:
                schema_editor.add_field(model, registry._field_registry[fld])
                transaction.savepoint_commit(sid)
        except ProgrammingError:
            transaction.savepoint_rollback(sid)
            continue
