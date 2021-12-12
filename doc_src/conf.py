"""
Sphinx configuration.
"""

import os
import sys
from datetime import date
from pathlib import Path

project_root = Path("..").resolve()
sys.path.insert(0, str(project_root / "example"))
sys.path.insert(0, str(project_root))
os.environ["DJANGO_SETTINGS_MODULE"] = "example.settings"

# Setup Django
import django  # NOQA

django.setup()

import categories  # noqa
import categories.urls  # noqa

project = "Django Categories"
copyright = f"2010-{date.today():%Y}, Corey Oordt"

version = categories.__version__
release = categories.__version__

# -- General configuration -----------------------------------------------------

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.coverage",
    "sphinx.ext.githubpages",
    "sphinxcontrib_django2",
]
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2
autosummary_generate = True
napoleon_attr_annotations = True
napoleon_include_special_with_doc = False
napoleon_include_private_with_doc = True
napoleon_include_init_with_doc = True
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "django": (
        "https://docs.djangoproject.com/en/stable",
        "https://docs.djangoproject.com/en/stable/_objects",
    ),
}

templates_path = ["_templates"]
source_suffix = [".rst", ".md"]
master_doc = "index"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = "sphinx"
todo_include_todos = False


# -- Options for HTML output ---------------------------------------------------

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = [
    "css/custom.css",
]
