from django.core.management.base import BaseCommand, CommandError
from categories.models import Category
from django.template.defaultfilters import slugify
from django.db import transaction

class Command(BaseCommand):
    """Import category trees from a file."""
    
    help = "Imports category tree(s) from a file. Sub categories must be indented by the same multiple of spaces or tabs."
    args = "file_path [file_path ...]"
    
    def get_indent(self, string):
        """
        Look through the string and count the spaces
        """
        indent_amt = 0
        
        if string[0] == '\t':
            return '\t'
        for char in string:
            if char == ' ':
                indent_amt += 1
            else:
                return ' ' * indent_amt
    
    @transaction.commit_on_success
    def make_category(self, string, parent=None, order=1):
        """
        Make and save a category object from a string
        """
        cat = Category(
            name=string.strip(),
            slug=slugify(string.strip())[:49],
            #parent=parent,
            order=order
        )
        cat._tree_manager.insert_node(cat, parent, 'last-child', True)
        cat.save()
        if parent:
            parent.rght = cat.rght + 1
            parent.save()
        return cat
    
    def parse_lines(self, lines):
        """
        Do the work of parsing each line
        """
        indent = ''
        level = 0
        
        if lines[0][0] == ' ' or lines[0][0] == '\t':
            raise CommandError("The first line in the file cannot start with a space or tab.")
        
        # This keeps track of the current parents at a given level
        current_parents = {0: None}
        
        for line in lines:
            if len(line) == 0:
                continue
            if line[0] == ' ' or line[0] == '\t':
                if indent == '':
                    indent = self.get_indent(line)
                elif not line[0] in indent:
                    raise CommandError("You can't mix spaces and tabs for indents")
                level = line.count(indent)
                current_parents[level] = self.make_category(line, parent=current_parents[level-1])
            else:
                # We are back to a zero level, so reset the whole thing
                current_parents = {0: self.make_category(line)}
        current_parents[0]._tree_manager.rebuild()
    
    def handle(self, *file_paths, **options):
        """
        Handle the basic import
        """
        import os
        
        for file_path in file_paths:
            if not os.path.isfile(file_path):
                print "File %s not found." % file_path
                continue
            f = file(file_path, 'r')
            data = f.readlines()
            f.close()
            
            self.parse_lines(data)
            