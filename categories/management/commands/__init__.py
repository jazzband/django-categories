try:
    from south.db import db  # noqa
    from django.db.models.signals import post_syncdb  # noqa
    from categories.migration import migrate_app  # noqa

    post_syncdb.connect(migrate_app)
except ImportError:
    pass
