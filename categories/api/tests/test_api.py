# import get_user_model
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase

from categories.models import Category

User = get_user_model()


class MeViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser("test-user", "foo@bar.baz", "test-password")
        self.client.force_authenticate(user=self.user)

        category = Category.tree.create(name="Foo category", slug="foo_category", active=True, order=0, parent=None)
        baker.make(
            "SimpleText",
            primary_category=category,
        )
        cache.clear()

    def test_list(self):
        """
        Test list
        """
        url = reverse("categories-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual(
            response.json(),
            [
                {
                    "name": "Foo category",
                    "slug": "foo_category",
                    "active": True,
                    "thumbnail": None,
                    "thumbnail_width": None,
                    "thumbnail_height": None,
                    "order": 0,
                    "alternate_title": "",
                    "alternate_url": "",
                    "description": None,
                    "meta_keywords": "",
                    "meta_extra": "",
                    "children": [],
                    "flatpage_count": 0,
                    "flatpage_count_cumulative": 0,
                    "other_cats_count": 0,
                    "other_cats_count_cumulative": 0,
                    "more_cats_count": 0,
                    "more_cats_count_cumulative": 0,
                    "simpletext_count": 1,
                    "simpletext_count_cumulative": 1,
                    "simpletext_sec_cat_count": 0,
                    "simpletext_sec_cat_count_cumulative": 0,
                }
            ],
        )
