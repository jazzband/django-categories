"""
>>> from ellington.categories.models import *

>>> news = Hierarchy.objects.get(slug="news")
>>> news.get_all_categories()
[<Category: [News] /LOLcats>, <Category: [News] /Monster Attacks>, <Category: [News] /Weather>, <Category: [News] /Weather/Disasters>, <Category: [News] /Weather/Disasters/Mothra>]

>>> news.get_toplevel_categories()
[<Category: [News] /Monster Attacks>, <Category: [News] /Weather>]

>>> weather = news.get_category_from_slug("/weather")
>>> weather
<Category: [News] /Weather>

>>> from django.test import Client
>>> c = Client()
>>> r = c.get('/categories/')
>>> r.context[0]['object_list']
[<Hierarchy: News>]
>>> r = c.get('/categories/news/')
>>> r.context[0]['object']
<Hierarchy: News>
"""

__fixtures__ = ['categories.yaml']
