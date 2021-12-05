from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from django.test import Client, RequestFactory, TestCase

from categories import views
from categories.models import Category, CategoryRelation


class MyCategoryRelationView(views.CategoryRelatedDetail):
    model = CategoryRelation


class TestCategoryViews(TestCase):
    fixtures = [
        "musicgenres.json",
    ]

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

    def test_category_detail(self):
        cat0 = Category.objects.get(slug="country", level=0)
        cat1 = cat0.children.get(slug="country-pop")
        cat2 = Category.objects.get(slug="urban-cowboy")
        url = cat0.get_absolute_url()
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        url = cat1.get_absolute_url()
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        url = cat2.get_absolute_url()
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        response = self.client.get("%sfoo/" % url)
        self.assertEquals(response.status_code, 404)

    def test_get_category_for_path(self):
        cat0 = Category.objects.get(slug="country", level=0)
        cat1 = cat0.children.get(slug="country-pop")
        cat2 = Category.objects.get(slug="urban-cowboy")

        result = views.get_category_for_path("/country/country-pop/urban-cowboy/")
        self.assertEquals(result, cat2)
        result = views.get_category_for_path("/country/country-pop/")
        self.assertEquals(result, cat1)
        result = views.get_category_for_path("/country/")
        self.assertEquals(result, cat0)

    def test_categorydetailview(self):
        request = self.factory.get("")
        request.user = AnonymousUser()
        self.assertRaises(AttributeError, views.CategoryDetailView.as_view(), request)

        request = self.factory.get("")
        request.user = AnonymousUser()
        response = views.CategoryDetailView.as_view()(request, path="/country/country-pop/urban-cowboy/")
        self.assertEquals(response.status_code, 200)

        request = self.factory.get("")
        request.user = AnonymousUser()
        self.assertRaises(Http404, views.CategoryDetailView.as_view(), request, path="/country/country-pop/foo/")

    def test_categoryrelateddetailview(self):
        from simpletext.models import SimpleText

        stext = SimpleText.objects.create(name="Test", description="test description")
        cat = Category.objects.get(slug="urban-cowboy")
        cat_rel = CategoryRelation.objects.create(category=cat, content_object=stext)  # NOQA
        request = self.factory.get("")
        request.user = AnonymousUser()
        self.assertRaises(AttributeError, MyCategoryRelationView.as_view(), request)

        request = self.factory.get("")
        request.user = AnonymousUser()
        response = MyCategoryRelationView.as_view()(request, category_path="/country/country-pop/urban-cowboy/")
        self.assertEquals(response.status_code, 200)

        request = self.factory.get("")
        request.user = AnonymousUser()
        self.assertRaises(
            Http404, MyCategoryRelationView.as_view(), request, category_path="/country/country-pop/foo/"
        )
