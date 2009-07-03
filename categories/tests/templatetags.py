from ellington.core.utils.test import TemplateTestCase

class GetCategory(TemplateTestCase):

    fixtures = ['categories.yaml']

    def test_too_few_arguments(self):
        """Ensure that get_cateogry bails is we don't give it enough arguments."""
        ex = self.render('{% load categories %}{% get_category %}')
        self.assertEqual(str(ex), 'get_category tag requires at least three arguments.')
        self.assertTemplateSyntaxError(ex)

    def test_as(self):
        """Test that the second argument to get_category is 'as'."""
        ex = self.render('{% load categories %}{% get_category "foo" notas bar %}')
        self.assertEqual(str(ex), "get_category tag requires the third argument to be 'as'.")
        self.assertTemplateSyntaxError(ex)

    def test_wrong_length(self):
        """Test that calling get_category with the wrong number of arguments properly raises an exception."""
        ex = self.render('{% load categories %}{% get_category one as three hierarchy four five %}')
        self.assertEqual(str(ex), "get_category tag requires exactly 3, or 5 arguments.")
        self.assertTemplateSyntaxError(ex)
        ex2 = self.render('{% load categories %}{% get_category one as three four five six seven %}')
        self.assertEqual(str(ex2), "get_category tag requires exactly 3, or 5 arguments.")
        self.assertTemplateSyntaxError(ex2)

    def test_basic_usage(self):
        """Test that we can properly retrieve a category with the default hierarchy."""
        resp = self.render('{% load categories %}{% get_category "/monster-attacks" as cat %}{{ cat }}')
        self.assertEqual(resp, u'[News] /Monster Attacks')

    def test_hierarchy(self):
        """Verify that we can summon Mothra."""
        resp = self.render('{% load categories %}{% get_category "/weather/disasters/mothra" as cat hierarchy "news" %}{{ cat }}')
        self.assertEqual(resp, u'[News] /Weather/Disasters/Mothra')
