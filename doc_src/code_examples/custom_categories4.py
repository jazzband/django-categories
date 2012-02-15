def save(self, *args, **kwargs):
    if self.thumbnail:
        from django.core.files.images import get_image_dimensions
        import django
        if django.VERSION[1] < 2:
            width, height = get_image_dimensions(self.thumbnail.file)
        else:
            width, height = get_image_dimensions(self.thumbnail.file, close=True)
    else:
        width, height = None, None
    
    self.thumbnail_width = width
    self.thumbnail_height = height
    
    super(Category, self).save(*args, **kwargs)