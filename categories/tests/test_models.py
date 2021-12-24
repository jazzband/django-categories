import os

from django.core.files import File
from django.core.files.uploadedfile import UploadedFile
from django.test import TestCase

from categories.models import Category


class TestCategoryThumbnail(TestCase):
    def test_thumbnail(self):

        file_name = "test_image.jpg"

        with open(os.path.join(os.path.dirname(__file__), file_name), "rb") as f:
            test_image = UploadedFile(File(f), content_type="image/jpeg")
            category = Category.objects.create(name="Test Category", slug="test-category", thumbnail=test_image)
            self.assertEqual(category.pk, 1)
            self.assertEqual(category.thumbnail_width, 640)
            self.assertEqual(category.thumbnail_height, 480)
