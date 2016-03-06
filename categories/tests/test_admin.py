from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from categories.models import Category


class TestCategoryAdmin(TestCase):

    def setUp(self):
        self.client = Client()

    def test_adding_parent_and_child(self):
        User.objects.create_superuser('testuser', 'testuser@example.com', 'password')
        self.client.login(username='testuser', password='password')
        url = reverse('admin:categories_category_add')
        data = {
            'parent': '',
            'name': "Parent",
            'thumbnail': '',
            'filename': '',
            'active': 'on',
            'alternate_title': '',
            'alternate_url': '',
            'description': '',
            'meta_keywords': '',
            'meta_extra': '',
            'order': 0,
            'slug': 'parent',
            '_save': '_save',
        }
        resp = self.client.post(url, data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(1, Category.objects.count())

        # update parent
        data.update({'name': 'Parent (Changed)'})
        resp = self.client.post(reverse('admin:categories_category_change', args=(1,)), data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(1, Category.objects.count())

        # add a child
        data.update({
            'parent': '1',
            'name': 'Child',
            'slug': 'child',
        })
        resp = self.client.post(url, data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(2, Category.objects.count())

        # update child
        data.update({'name': 'Child (Changed)'})
        resp = self.client.post(reverse('admin:categories_category_change', args=(2,)), data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(2, Category.objects.count())
