from django.db import models, DatabaseError
from django.core.exceptions import ImproperlyConfigured


def migrate_app(sender, app, created_models, verbosity, *args, **kwargs):
    """
    Migrate all models of this app registered
    """
    from .fields import CategoryM2MField, CategoryFKField
    from .models import Category
    from .settings import FIELD_REGISTRY
    import sys
    import StringIO

    org_stderror = sys.stderr
    sys.stderr = StringIO.StringIO()  # south will print out errors to stderr
    try:
        from south.db import db
    except ImportError:
        raise ImproperlyConfigured("South must be installed for this command to work")
    # pull the information from the registry
    app_name = app.__name__.split('.')[-2]

    fields = [fld for fld in FIELD_REGISTRY.keys() if fld.startswith(app_name)]
    # call the south commands to add the fields/tables
    for fld in fields:
        app_name, model_name, field_name = fld.split('.')

        # Table is typically appname_modelname, but it could be different
        #   always best to be sure.
        mdl = models.get_model(app_name, model_name)

        if isinstance(FIELD_REGISTRY[fld], CategoryFKField):
            try:
                db.start_transaction()
                table_name = mdl._meta.db_table
                FIELD_REGISTRY[fld].default = -1
                db.add_column(table_name, field_name, FIELD_REGISTRY[fld], keep_default=False)
                db.commit_transaction()
                if verbosity:
                    print "Added ForeignKey %s to %s" % (field_name, model_name)
            except DatabaseError, e:
                db.rollback_transaction()
                if "already exists" in str(e):
                    if verbosity > 1:
                        print "ForeignKey %s to %s already exists" % (field_name, model_name)
                else:
                    sys.stderr = org_stderror
                    raise e
        elif isinstance(FIELD_REGISTRY[fld], CategoryM2MField):
            table_name = "%s_%s" % (mdl._meta.db_table, 'categories')
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
                    print "Added Many2Many table between %s and %s" % (model_name, 'category')
            except DatabaseError, e:
                db.rollback_transaction()
                if "already exists" in str(e):
                    if verbosity > 1:
                        print "Many2Many table between %s and %s already exists" % (model_name, 'category')
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
    from .settings import FIELD_REGISTRY
    try:
        from south.db import db
    except ImportError:
        raise ImproperlyConfigured("South must be installed for this command to work")
    mdl = models.get_model(app_name, model_name)

    fld = "%s.%s.%s" % (app_name, model_name, field_name)

    if isinstance(FIELD_REGISTRY[fld], CategoryFKField):
        print "Dropping ForeignKey %s from %s" % (field_name, model_name)
        try:
            db.start_transaction()
            table_name = mdl._meta.db_table
            db.delete_column(table_name, field_name)
            db.commit_transaction()
        except DatabaseError, e:
            db.rollback_transaction()
            raise e
    elif isinstance(FIELD_REGISTRY[fld], CategoryM2MField):
        print "Dropping Many2Many table between %s and %s" % (model_name, 'category')
        table_name = "%s_%s" % (mdl._meta.db_table, 'categories')
        try:
            db.start_transaction()
            db.delete_table(table_name, cascade=False)
            db.commit_transaction()
        except DatabaseError, e:
            db.rollback_transaction()
            raise e
