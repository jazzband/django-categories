class CategoryAdminForm(CategoryBaseAdminForm):
    class Meta:
        model = Category
    
    def clean_alternate_title(self):
        if self.instance is None or not self.cleaned_data['alternate_title']:
            return self.cleaned_data['name']
        else:
            return self.cleaned_data['alternate_title']