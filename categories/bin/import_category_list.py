#!/usr/bin/env python2.3

import os
import sys
from ellington.categories.models import Hierarchy, Category, slugify, slugify_path, get_path_bits

hierarchy_slug = sys.argv[1]
filename = sys.argv[2]

try:
    this_hierarchy = Hierarchy.objects.get(slug=hierarchy_slug)
except Hierarchy.DoesNotExist:
    print "Hierarchy %s not found!" % hierarchy_slug
    sys.exit(1)

if not os.path.isfile(filename):
    print "File %s not found." % filename
    sys.exit(1)

f = file(sys.argv[2], 'r')
data = f.readlines()
f.close()

count = 0
for line in data:
    recursive_paths = Category.objects.get_recursive_paths(line)
    for path in recursive_paths:
        try:
            this_hierarchy.get_category_from_slug(slugify_path(path))
        except Category.DoesNotExist:
            #print "%s did not exist" % path
            #continue
            bits = get_path_bits(path)
            if len(bits) > 1:
                # parent *should* exist at this point
                parent = this_hierarchy.get_category_from_slug(
                    slugify_path('/%s' % '/'.join(bits[:-1]))
                )
            else:
                parent = None
            c = Category.objects.create(
                hierarchy=this_hierarchy,
                name=bits[-1],
                slug=slugify(bits[-1]),
                parent=parent,
            )
            count += 1
            print "Created %s (%s)" % (path, count)
print "%s categories imported." % count
