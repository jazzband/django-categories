from categories.models import CategoryBase

class SimpleCategory(CategoryBase):
    """
    A simple of catgorizing example
    """
    
    class Meta:
        verbose_name_plural = 'simple categories'
