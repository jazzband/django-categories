from django.test import TestCase

from ..utils import slugify


class TestSlugify(TestCase):
    def test_slugify(self):
        string_dict = {
            "naïve café": "naïve-café",
            "spaced    out": "spaced-out",
            "user@domain.com": "userdomaincom",
            "100% natural": "100-natural",
            "über-cool": "über-cool",
            "façade élégant": "façade-élégant",
            "北京大学": "北京大学",
            "Толстой": "толстой",
            "ñoño": "ñoño",
            "سلام": "سلام",
            "Αθήνα": "αθήνα",
            "こんにちは": "こんにちは",
            "˚č$'\\*>%ˇ'!/": "čˇ",
        }
        for key, value in string_dict.items():
            self.assertEqual(slugify(key), value)
