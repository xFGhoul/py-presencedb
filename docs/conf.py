# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "py-presencedb"
copyright = "2023, Ghoul"
author = "Ghoul"

import os
import sys

sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.abspath("extensions"))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "builder",
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinxcontrib_trio",
    "details",
    "exception_hierarchy",
    "attributetable",
    "resourcelinks",
    "nitpick_file_ignorer",
    "colour_preview",
]

autodoc_member_order = "bysource"
autodoc_typehints = "none"
# maybe consider this?
# napoleon_attr_annotations = False

extlinks = {
    "issue": ("https://github.com/xFGhoul/py-presencedb/issues/%s", "GH-"),
}
# Links used for cross-referencing stuff in other documentation
intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None),
    "aio": ("https://docs.aiohttp.org/en/stable/", None),
    "req": ("https://requests.readthedocs.io/en/latest/", None),
}

rst_prolog = """
.. |coro| replace:: This function is a |coroutine_link|_.
.. |maybecoro| replace:: This function *could be a* |coroutine_link|_.
.. |coroutine_link| replace:: *coroutine*
.. _coroutine_link: https://docs.python.org/3/library/asyncio-task.html#coroutine
"""

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

master_doc = "index"

nitpick_ignore_files = [
    "migrating_to_async",
    "migrating_to_v1",
    "migrating",
    "whats_new",
]
html_theme = "basic"

html_context = {
    "discord_invite": "https://discord.com",
}

resource_links = {
    "discord": "https://discord.com/users/433026067050266634",
    "issues": "https://github.com/xFGhoul/py-presencedb/issues",
    "discussions": "https://github.com/xFGhoul/py-presencedb/discussions",
    "examples": "https://github.com/xFGhoul/py-presencedb/dev/examples",
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ["_static"]

html_search_scorer = "_static/scorer.js"

html_js_files = ["custom.js", "settings.js", "copy.js", "sidebar.js"]

man_pages = [("index", "presencedb", "presencedb Documentation", ["Ghoul"], 1)]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "presencedb",
        "presencedb Documentation",
        "Ghoul",
        "presencedb",
        "One line description of project.",
        "Miscellaneous",
    ),
]
