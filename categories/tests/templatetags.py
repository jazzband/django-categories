from django.test import TestCase
from django import template


class GetCategoryTest(TestCase):
    
    fixtures = ['musicgenres.json']
    
    def render_template(self, template_string, context={}):
        """
        Return the rendered string or raise an exception.
        """
        tpl = template.Template(template_string)
        ctxt = template.Context(context)
        return tpl.render(ctxt)

    def testTooFewArguments(self):
        """
        Ensure that get_cateogry raises an exception if there aren't enough arguments.
        """
        self.assertRaises(template.TemplateSyntaxError, self.render_template, '{% load category_tags %}{% get_category %}')

    def testTooManyArguments(self):
        """
        Ensure that get_category raises an exception if there are too many arguments.
        """
        self.assertRaises(template.TemplateSyntaxError, self.render_template, '{% load category_tags %}{% get_category "/Rock" as too many arguments %}')

    def testAsIsSecondArgument(self):
        """
        Test that the second argument to get_category is 'as'.
        """
        self.assertRaises(template.TemplateSyntaxError, self.render_template, '{% load category_tags %}{% get_category "Rock" notas rock %}')

    def testBasicUsage(self):
        """
        Test that we can properly retrieve a category.
        """
        rock_resp = u'\n<ul><li><a href="/categories/">Top</a>\n</li></ul>'
        resp = self.render_template('{% load category_tags %}{% display_path_as_ul "/Rock" %}')
        self.assertEqual(resp, rock_resp)
        