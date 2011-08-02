from django.db.models.signals import post_syncdb
from categories.migration import migrate_app

post_syncdb.connect(migrate_app)
