#!/usr/bin/env python

from ellington.categories.models import Category

roots = Category.objects.filter(parent__isnull=True)

for root in roots:
    root.refresh_paths(force=True)

