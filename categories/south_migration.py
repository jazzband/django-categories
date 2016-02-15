from django.db import models, DatabaseError
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _


def migrate_app(sender, app, created_models=None, verbosity=False, *args, **kwargs):
    """
    Migrate all models of this app registered
    """
    from .fields import CategoryM2MField, CategoryFKField
    from .models import Category
    from .registration import registry
    import sys
    import io

    org_stderror = sys.stderr
    sys.stderr = io.StringIO()  # south will print out errors to stderr
    try:
        from south.db import db
    except ImportError:
        raise ImproperlyConfigured(_('%(dependency)s must be installed for this command to work') %
                                   {'dependency': 'South'})
    # pull the information from the registry
    if isinstance(app, str):
        app_name = app
    else:
        app_name = app.__name__.split('.')[-2]

    fields = [fld for fld in list(registry._field_registry.keys()) if fld.startswith(app_name)]
    # call the south commands to add the fields/tables
    for fld in fields:
        app_name, model_name, field_name = fld.split('.')

        # Table is typically appname_modelname, but it could be different
        #   always best to be sure.
        mdl = models.get_model(app_name, model_name)

        if isinstance(registry._field_registry[fld], CategoryFKField):
            try:
                db.start_transaction()
                table_name = mdl._meta.db_table
                registry._field_registry[fld].default = -1
                db.add_column(table_name, field_name, registry._field_registry[fld], keep_default=False)
                db.commit_transaction()
                if verbosity:
                    print((_('Added ForeignKey %(field_name)s to %(model_name)s') %
                           {'field_name': field_name, 'model_name': model_name}))
            except DatabaseError as e:
                db.rollback_transaction()
                if "already exists" in str(e):
                    if verbosity > 1:
                        print((_('ForeignKey %(field_name)s to %(model_name)s already exists') %
                               {'field_name': field_name, 'model_name': model_name}))
                else:
                    sys.stderr = org_stderror
                    raise e
        elif isinstance(registry._field_registry[fld], CategoryM2MField):
            table_name = '%s_%s' % (mdl._meta.db_table, 'categories')
            try:
                db.start_transaction()
                db.create_table(table_name, (
                    ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
                    (model_name, models.ForeignKey(mdl, null=False)),
                    ('category', models.ForeignKey(Category, null=False))
                ))
                db.create_unique(table_name, ['%s_id' % model_name, 'category_id'])
                db.commit_transaction()
                if verbosity:
                    print((_('Added Many2Many table between %(model_name)s and %(category_table)s') %
                           {'model_name': model_name, 'category_table': 'category'}))
            except DatabaseError as e:
                db.rollback_transaction()
                if "already exists" in str(e):
                    if verbosity > 1:
                        print((_('Many2Many table between %(model_name)s and %(category_table)s already exists') %
                               {'model_name': model_name, 'category_table': 'category'}))
                else:
                    sys.stderr = org_stderror
                    raise e
    sys.stderr = org_stderror


def drop_field(app_name, model_name, field_name):
    """
    Drop the given field from the app's model
    """
    # Table is typically appname_modelname, but it could be different
    #   always best to be sure.
    from .fields import CategoryM2MField, CategoryFKField
    from .registration import registry
    try:
        from south.db import db
    except ImportError:
        raise ImproperlyConfigured(_('%(dependency)s must be installed for this command to work') %
                                   {'dependency': 'South'})
    mdl = models.get_model(app_name, model_name)

    fld = '%s.%s.%s' % (app_name, model_name, field_name)

    if isinstance(registry._field_registry[fld], CategoryFKField):
        print((_('Dropping ForeignKey %(field_name)s from %(model_name)s') %
               {'field_name': field_name, 'model_name': model_name}))
        try:
            db.start_transaction()
            table_name = mdl._meta.db_table
            db.delete_column(table_name, field_name)
            db.commit_transaction()
        except DatabaseError as e:
            db.rollback_transaction()
            raise e
    elif isinstance(registry._field_registry[fld], CategoryM2MField):
        print((_('Dropping Many2Many table between %(model_name)s and %(category_table)s') %
               {'model_name': model_name, 'category_table': 'category'}))
        try:
            db.start_transaction()
            db.delete_table(table_name, cascade=False)
            db.commit_transaction()
        except DatabaseError as e:
            db.rollback_transaction()
            raise e
