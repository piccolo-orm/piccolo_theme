# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import datetime
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

project = 'Piccolo Theme'
year = datetime.datetime.now().year
copyright = f'{year}, Daniel Townsend'
author = 'Daniel Townsend'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'breathe'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'piccolo_theme'
html_short_title = 'Piccolo Theme'

html_theme_options = {
    "banner_text": (
        "This is an example notification banner - welcome to the Piccolo "
        "Theme!"
    ),
    "banner_hiding": "permanent",
    "show_theme_credit": True,
    "git_url": "https://github.com/piccolo-orm/piccolo_theme/",
    "is_github": True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

breathe_projects = {
    "cpp_demo": "./cpp_breathe_demo",
    "c_demo": "./c_breathe_demo"
}
breathe_default_project = "cpp_demo"
breathe_domain_by_extension = {
    "h": "c",
    "c": "c",
    "hpp": "cpp",
    "cpp": "cpp"
}
