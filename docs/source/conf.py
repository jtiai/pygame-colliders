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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('../..'))

from distutils.version import LooseVersion

import cloud_sptheme as csp
import pygame_colliders

# -- Project information -----------------------------------------------------

project = 'Pygame Colliders'
copyright = '2020, Jani Tiainen'
author = 'Jani Tiainen'

# The full version, including alpha/beta/rc tags

release = LooseVersion(pygame_colliders.__version__).vstring


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # cloud's extensions
    'cloud_sptheme.ext.autodoc_sections',
    'cloud_sptheme.ext.relbar_links',
    'cloud_sptheme.ext.escaped_samp_literals',
    'cloud_sptheme.ext.issue_tracker',
    'cloud_sptheme.ext.table_styling',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.autosectionlabel',

    # 3rd party extensions
    'sphinxcontrib.fulltoc',
    'sphinx.ext.viewcode',  # mainly to make sure layout works properly

    # cloud's extensions
    'cloud_sptheme.ext.autodoc_sections',
    'cloud_sptheme.ext.relbar_links',
    'cloud_sptheme.ext.escaped_samp_literals',
    'cloud_sptheme.ext.issue_tracker',
    'cloud_sptheme.ext.table_styling',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

master_doc = "contents"

index_doc = "index"

source_encoding = "utf-8"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'cloud'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    "css/custom.css",
]

html_theme_options = {
    "roottarget": "index",
    "borderless_decor": True,
    "sidebarwidth": "3in",
    "hyphenation_language": "en",
}

html_theme_path = [csp._theme_dir]

html_use_smartypants = True

html_theme_options = {
    "linkcolor": "light-blue",
}

# Custom sidebar templates, maps document names to template names.
html_sidebars = {'**': ['searchbox.html', 'globaltoc.html']}
