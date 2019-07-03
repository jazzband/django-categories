
from __future__ import absolute_import, unicode_literals

from django.utils.html import escape
from django.utils.safestring import mark_safe
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from wiki.core.plugins.base import PluginSidebarFormMixin
from wiki.models import Article, ArticleRevision, URLPath
from .models import ArticleCategory
from wiki.plugins.metadata.models import deepest_instance

# It would be cleaner if we combined the SidebarForm and EditCategoryForm, however the logic of
# the form might be too complex if we do

class ArticleCategoryForm(forms.ModelForm):
    '''Simple model form for category creation, edit this to hide fields that are unnecessary.
    Landing article creation handled in views.py: form_valid()'''

    class Meta:
        model = ArticleCategory
        exclude = ('article',)

class SidebarForm(PluginSidebarFormMixin):

    # Because the many-to-many field is defined on ArticleCategory, and
    # we want to display a form for the Article, we need to create a field here:
    # (https://stackoverflow.com/a/2264722)
    categories = forms.ModelMultipleChoiceField(queryset=ArticleCategory.objects.all())

    ''' This edit form allows us to change what categories an article is in '''
    def __init__(self, article, request, *args, **kwargs):
        self.validCategory = True
        self.article = article
        self.request = request
        super(SidebarForm, self).__init__(*args, **kwargs)
        self.fields['categories'].required = False
        self.fields['categories'].label_from_instance = lambda obj: mark_safe("%s" % escape(obj.short_title) + (' <a href="/'+str(obj.article.urlpath_set.all()[0])+'" target="_blank">View</a>'))
        self.fields['categories'].initial = article.categories.all()
        self.fields['categories'].widget = forms.CheckboxSelectMultiple()
        ids = self.article.category.subtree_ids() if hasattr(self.article, 'category') else []
        self.fields['categories'].queryset = ArticleCategory.objects.exclude(id__in = ids)
        if not self.article.categories.all():
            self.validCategory = False


    def get_usermessage(self):
        return ugettext(
            "New category set.")

    def save(self, *args, **kwargs):
        if self.is_valid():
            data = self.cleaned_data
            field = data['categories']
            self.article.categories = field
            self.article.save()
        return super(SidebarForm, self).save(*args, **kwargs)

    class Meta:
        model = Article
        fields = ('categories',)

class EditCategoryForm(PluginSidebarFormMixin):
    ''' This edit form allows us to change the parent category of a category
        via the edit screen of its category landing article'''

    def __init__(self, article, request, *args, **kwargs):
        self.article = article
        self.request = request
        self.validCategory = hasattr(self.article, 'category')
        super(EditCategoryForm, self).__init__(*args, **kwargs)

        if not self.validCategory:
            return

        self.fields['parent'].label_from_instance = lambda obj: mark_safe("%s" %  obj.parent.short_title + '/' + obj.short_title if not obj.parent is None else obj.short_title)
        self.fields['parent'].initial = article.category.parent

        # remove the category itself and its descendants from the available choices
        ids = article.category.subtree_ids()
        self.fields['parent'].queryset = ArticleCategory.objects.exclude(id__in = ids) #.exclude(slug = article.category.slug)

    def save(self, *args, **kwargs):
        self.instance = self.article.category
        data = self.cleaned_data
        oldparent = self.instance.parent
        newparent = data['parent']
        if newparent!=oldparent: # parent has changed
            # make a new revision of the article to record the change
            revision = ArticleRevision()
            revision.inherit_predecessor(self.article)
            revision.set_from_request(self.request)
            revision.parent = newparent
            revision.categories = self.article.categories
            if oldparent:
                oldparent = oldparent.name
            revision.automatic_log = f'Parent Category: {oldparent} → {newparent.name} (not revertible)'
            self.article.add_revision(revision)
            # reverting to a previous revision from the Changes page currently does not affect the category parent
        self.instance.parent = newparent
        self.instance.save()
        super(EditCategoryForm, self).save(*args, **kwargs)

    class Meta:
        model = ArticleCategory
        fields = ('parent',)
