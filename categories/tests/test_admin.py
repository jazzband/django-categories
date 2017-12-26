# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client, TestCase
from django.utils.encoding import smart_text

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
            'name': smart_text('Parent Catégory'),
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
            'categoryrelation_set-TOTAL_FORMS': '0',
            'categoryrelation_set-INITIAL_FORMS': '0',
            'categoryrelation_set-MIN_NUM_FORMS': '1000',
            'categoryrelation_set-MAX_NUM_FORMS': '1000',
        }
        resp = self.client.post(url, data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(1, Category.objects.count())

        # update parent
        data.update({'name': smart_text('Parent Catégory (Changed)')})
        resp = self.client.post(reverse('admin:categories_category_change', args=(1,)), data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(1, Category.objects.count())

        # add a child
        data.update({
            'parent': '1',
            'name': smart_text('Child Catégory'),
            'slug': smart_text('child-category'),
        })
        resp = self.client.post(url, data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(2, Category.objects.count())

        # update child
        data.update({'name': 'Child (Changed)'})
        resp = self.client.post(reverse('admin:categories_category_change', args=(2,)), data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(2, Category.objects.count())

        # test the admin list view
        url = reverse('admin:categories_category_changelist')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
