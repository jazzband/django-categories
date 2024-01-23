# Storages used for testing THUMBNAIL_STORAGE and THUMBNAIL_STORAGE_ALIAS
from django.core.files.storage import FileSystemStorage


class MyTestStorage(FileSystemStorage):
    pass


class MyTestStorageAlias(FileSystemStorage):
    pass
