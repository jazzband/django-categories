from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.test.utils import override_settings
from django.urls import reverse
from django.utils.encoding import smart_str

from categories.models import Category


class TestCategoryAdmin(TestCase):
    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser("testuser", "testuser@example.com", "password")

    def test_adding_parent_and_child(self):
        self.client.login(username="testuser", password="password")
        url = reverse("admin:categories_category_add")
        data = {
            "parent": "",
            "name": smart_str("Parent Catégory"),
            "thumbnail": "",
            "filename": "",
            "active": "on",
            "alternate_title": "",
            "alternate_url": "",
            "description": "",
            "meta_keywords": "",
            "meta_extra": "",
            "order": 0,
            "slug": "parent",
            "_save": "_save",
            "categoryrelation_set-TOTAL_FORMS": "0",
            "categoryrelation_set-INITIAL_FORMS": "0",
            "categoryrelation_set-MIN_NUM_FORMS": "1000",
            "categoryrelation_set-MAX_NUM_FORMS": "1000",
        }
        resp = self.client.post(url, data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(1, Category.objects.count())

        # update parent
        data.update({"name": smart_str("Parent Catégory (Changed)")})
        resp = self.client.post(reverse("admin:categories_category_change", args=(1,)), data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(1, Category.objects.count())

        # add a child
        data.update(
            {
                "parent": "1",
                "name": smart_str("Child Catégory"),
                "slug": smart_str("child-category"),
            }
        )
        resp = self.client.post(url, data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(2, Category.objects.count())

        # update child
        data.update({"name": "Child (Changed)"})
        resp = self.client.post(reverse("admin:categories_category_change", args=(2,)), data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(2, Category.objects.count())

        # test the admin list view
        url = reverse("admin:categories_category_changelist")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    @override_settings(RELATION_MODELS=True)
    def test_addview_get(self):
        self.client.force_login(self.superuser)
        url = reverse("admin:categories_category_add")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, '<tr class="row1 ">')
        self.assertContains(
            resp,
            '<input type="number" name="categoryrelation_set-0-object_id" class="vIntegerField" '
            'min="0" id="id_categoryrelation_set-0-object_id">',
            html=True,
        )
