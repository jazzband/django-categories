"""Django application setup."""
from django.apps import AppConfig


class CategoriesConfig(AppConfig):
    """Application configuration for categories."""

    name = "categories"
    verbose_name = "Categories"

    def __init__(self, *args, **kwargs):
        super(CategoriesConfig, self).__init__(*args, **kwargs)
        from django.db.models.signals import class_prepared

        class_prepared.connect(handle_class_prepared)

    def ready(self):
        """Migrate the app after it is ready."""
        from django.db.models.signals import post_migrate

        from .migration import migrate_app

        post_migrate.connect(migrate_app)


def handle_class_prepared(sender, **kwargs):
    """
    See if this class needs registering of fields.
    """
    from .registration import registry
    from .settings import FK_REGISTRY, M2M_REGISTRY

    sender_app = sender._meta.app_label
    sender_name = sender._meta.model_name

    for key, val in list(FK_REGISTRY.items()):
        app_name, model_name = key.split(".")
        if app_name == sender_app and sender_name == model_name:
            registry.register_model(app_name, sender, "ForeignKey", val)

    for key, val in list(M2M_REGISTRY.items()):
        app_name, model_name = key.split(".")
        if app_name == sender_app and sender_name == model_name:
            registry.register_model(app_name, sender, "ManyToManyField", val)
