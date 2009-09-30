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
        rock_resp = u'Rock\rRock &gt; Surf rock\rRock &gt; Southern rock\rRock &gt; Soft rock\rRock &gt; Rock and roll\rRock &gt; Rap rock\rRock &gt; Punk rock\rRock &gt; Psychedelic rock\rRock &gt; Progressive rock\rRock &gt; Power pop\rRock &gt; Paisley Underground\rRock &gt; New Wave\rRock &gt; J-Rock\rRock &gt; Heavy metal\rRock &gt; Hard rock\rRock &gt; Glam rock\rRock &gt; Garage rock\rRock &gt; Folk rock\rRock &gt; Desert rock\rRock &gt; Dark cabaret\rRock &gt; C-Rock\rRock &gt; Blues-rock\rRock &gt; Alternative rock\r'
        resp = self.render_template('{% load category_tags %}{% get_category "/Rock" as cat_list %}{% for cat in cat_list %}{{ cat }}\r{% endfor %}')
        self.assertEqual(resp, rock_resp)
        
        crock_resp = u'Rock\rRock &gt; C-Rock\r'
        resp = self.render_template('{% load category_tags %}{% get_category "/Rock/C-Rock" as cat_list %}{% for cat in cat_list %}{{ cat }}\r{% endfor %}')
        self.assertEqual(resp, crock_resp)
        
        resp = self.render_template('{% load category_tags %}{% get_category %}')
        