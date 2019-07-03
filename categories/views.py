from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from django.template.loader import select_template
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, ListView

from wiki.models import URLPath, Article
from .models import ArticleCategory as Category
from . import forms


def category_detail(request, path, template_name='categories/category_detail.html', extra_context={}):
    path_items = path.strip('/').split('/')
    if len(path_items) >= 2:
        category = get_object_or_404(
            Category,
            slug__iexact=path_items[-1],
            level=len(path_items) - 1,
            parent__slug__iexact=path_items[-2])
    else:
        category = get_object_or_404(
            Category,
            slug__iexact=path_items[-1],
            level=len(path_items) - 1)

    templates = []
    while path_items:
        templates.append('categories/%s.html' % '_'.join(path_items))
        path_items.pop()
    templates.append(template_name)

    context = {'category': category}
    if extra_context:
        context.update(extra_context)
    return HttpResponse(select_template(templates).render(context))


def get_category_for_path(path, queryset=Category.objects.all()):
    path_items = path.strip('/').split('/')
    if len(path_items) >= 2:
        queryset = queryset.filter(
            slug__iexact=path_items[-1],
            level=len(path_items) - 1,
            parent__slug__iexact=path_items[-2])
    else:
        queryset = queryset.filter(
            slug__iexact=path_items[-1],
            level=len(path_items) - 1)
    return queryset.get()


class CategoryDetailView(DetailView):
    model = Category
    path_field = 'path'

    def get_object(self, **kwargs):
        if self.path_field not in self.kwargs:
            raise AttributeError("Category detail view %s must be called with "
                                 "a %s." % (self.__class__.__name__, self.path_field))
        if self.queryset is None:
            queryset = self.get_queryset()
        try:
            return get_category_for_path(self.kwargs[self.path_field], self.model.objects.all())
        except Category.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})

    def get_template_names(self):
        names = []
        path_items = self.kwargs[self.path_field].strip('/').split('/')
        while path_items:
            names.append('categories/%s.html' % '_'.join(path_items))
            path_items.pop()
        names.extend(super(CategoryDetailView, self).get_template_names())
        return names


class CategoryRelatedDetail(DetailView):
    path_field = 'category_path'
    object_name_field = None

    def get_object(self, **kwargs):
        if self.path_field not in self.kwargs:
            raise AttributeError("Category detail view %s must be called with "
                                 "a %s." % (self.__class__.__name__, self.path_field))
        queryset = super(CategoryRelatedDetail, self).get_queryset()
        try:
            category = get_category_for_path(self.kwargs[self.path_field])
        except Category.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return queryset.get(category=category)

    def get_template_names(self):
        names = []
        opts = self.object._meta
        path_items = self.kwargs[self.path_field].strip('/').split('/')
        if self.object_name_field:
            path_items.append(getattr(self.object, self.object_name_field))
        while path_items:
            names.append('%s/category_%s_%s%s.html' % (
                opts.app_label,
                '_'.join(path_items),
                opts.object_name.lower(),
                self.template_name_suffix)
            )
            path_items.pop()
        names.append('%s/category_%s%s.html' % (
            opts.app_label,
            opts.object_name.lower(),
            self.template_name_suffix)
        )
        names.extend(super(CategoryRelatedDetail, self).get_template_names())
        return names


class CategoryRelatedList(ListView):
    path_field = 'category_path'

    def get_queryset(self):
        if self.path_field not in self.kwargs:
            raise AttributeError("Category detail view %s must be called with "
                                 "a %s." % (self.__class__.__name__, self.path_field))
        queryset = super(CategoryRelatedList, self).get_queryset()
        category = get_category_for_path(self.kwargs[self.path_field])
        return queryset.filter(category=category)

    def get_template_names(self):
        names = []
        if hasattr(self.object_list, 'model'):
            opts = self.object_list.model._meta
            path_items = self.kwargs[self.path_field].strip('/').split('/')
            while path_items:
                names.append('%s/category_%s_%s%s.html' % (
                    opts.app_label,
                    '_'.join(path_items),
                    opts.object_name.lower(),
                    self.template_name_suffix)
                )
                path_items.pop()
            names.append('%s/category_%s%s.html' % (
                opts.app_label,
                opts.object_name.lower(),
                self.template_name_suffix)
            )
        names.extend(super(CategoryRelatedList, self).get_template_names())
        return names


class CategoryView( ArticleMixin, FormView ):

    ''' This view manages the creation of new categories '''

    form_class = forms.ArticleCategoryForm
    template_name = "category_detail.html"

    @method_decorator(get_article(can_read=True, can_create=True),)
    def dispatch(self, request, article, *args, **kwargs):
        categories = Category.objects.filter(slug="maincat")


        return super(
            CategoryView,
            self).dispatch(
            request,
            article,
            *args,
            **kwargs)

    def get_form_kwargs(self, **kwargs):
        kwargs = super(CategoryView, self).get_form_kwargs(**kwargs)
        #kwargs['article'] = self.article
        #kwargs['request'] = self.request
        return kwargs



    # Processing of category creation form goes here, modify the category creation process below
    def form_valid(self, form):
        clean_data = form.cleaned_data
        print(clean_data)
        slug = clean_data['slug']
        title = clean_data['name']
        content = clean_data['description']

        # creates an article for the category and then associates them by having equaling titles and slugs

        self.landing_article_urlpath = URLPath.create_article(
            URLPath.root(),
            slug,
            title = title,
            content = content,
            user_message = " ",
            user = self.request.user,
            article_kwargs = {'owner': self.request.user,
                              'group': self.article.group,
                              'group_read': self.article.group_read,
                              'group_write': self.article.group_write,
                              'other_read': self.article.other_read,
                              'other_write': self.article.other_write,
                              })
        landing_article = Article.objects.get(urlpath = self.landing_article_urlpath)
        form.instance.article = landing_article
        form.save()
        category = Category.objects.get(slug = slug)
        return redirect(
            "wiki:get",
            path=self.landing_article_urlpath.path,
            article_id=self.article.id)

    def get_form(self):
        form = super(CategoryView, self).get_form(form_class=forms.ArticleCategoryForm)
        return form


    # Insert form and category list into context for retrieval in template

    def get_context_data(self, **kwargs):
        kwargs['categories'] = Category.objects.all()
        kwargs['form'] = self.get_form()
        kwargs = super(CategoryView, self).get_context_data(**kwargs)
        kwargs['article'] = self.article
        return kwargs
