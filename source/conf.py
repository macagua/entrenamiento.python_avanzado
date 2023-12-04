# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath("sphinxext"))


# -- Project information -----------------------------------------------------
# General information about the project.
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project_namecode = "entrenamiento.python_avanzado"
project_short_name = "Programación en Python - Nivel avanzado"
project = project_short_name[0].capitalize() + project_short_name[1:38]
project_name = project_namecode.replace(".", "")
project_details = f"Entrenamiento de {project_short_name}"
publisher = "Leonardo J. Caballero G."
years = "2018 - 2023"
copyright = f"{years}, {publisher}"
author = "Leonardo J. Caballero G."

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "3.11"
# The full version, including alpha/beta/rc tags.
release = "3.11.5"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = "5.1.1"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # "IPython.sphinxext.ipython_console_highlighting",
    # "IPython.sphinxext.ipython_directive",
    "sphinx_contributors",
    "sphinx_immaterial",
    "sphinx_immaterial.kbd_keys",
    "sphinx_tabs.tabs",
    "sphinxcontrib.email",
    "sphinxcontrib.quizdown",
    "yasfb",
    "sphinx_disqus.disqus",
]

# Options for the linkcheck builder
# Ignore localhost
linkcheck_ignore = [
    r"http://localhost:\d+/",
    r"http://localhost:8080\d+/",
    r"http://localhost:5000",
    r"http://127.0.0.1:5000",
    r"http://localhost:8000",
    r"http://127.0.0.1:8000",
    r"http://localhost:8080",
    r"http://127.0.0.1:8080",
    r"http://localhost:8087",
    r"http://127.0.0.1:8087",
    r"http://whatever.herokuapp.com",
    r"http://example.com/news",
    r"http://example.com\d+/",
    r"acerca_de.html#sobre-el-instructor",
]
linkcheck_anchors = False
linkcheck_timeout = 30

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = {
    ".rst": "restructuredtext",
}

# The master toctree document.
root_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "es"

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = "%d de %B de %Y"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "build", "Thumbs.db", ".DS_Store", "index_latex.rst"]

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A string of reStructuredText that will be included at the end of every
# source file that is read.
rst_epilog = """
.. _`CodigoFacilito.com`: https://codigofacilito.com/
.. |psf| replace:: Python Software Foundation
"""

# If true, figures, tables and code-blocks are automatically numbered if
# they have a caption.
numfig = True

# A dictionary mapping 'figure', 'table', 'code-block' and 'section' to
# strings that are used for format of figure numbers. As a special character,
# %s will be replaced to figure number.
numfig_format = {
    "figure": "Figura %s,",
    "table": "Tabla %s,",
    "code-block": "Listado de código de bloque %s,",
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_immaterial"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "edit_uri": "edit/3/source",
    "repo_url": "https://github.com/macagua/entrenamiento.python_avanzado",
    "repo_name": "entrenamiento.python_avanzado",
    "repo_type": "github",
    "icon": {
        "repo": "fontawesome/brands/github",
    },
    "features": [
        "navigation.expand",
        "toc.integrate",
        "navigation.top",
        "navigation.tracking",
        "search.highlight",
        "search.share",
        "toc.follow",
        "toc.sticky",
    ],
    "palette": [
        {
            # Palette toggle for light mode
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            # "primary": "light-green",
            # "accent": "light-blue",
            "toggle": {
                "icon": "material/weather-sunny",
                "name": "Cambiar al modo oscuro",
            },
        },
        {
            # Palette toggle for dark mode
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            # "primary": "deep-orange",
            # "accent": "light",
            "toggle": {
                "icon": "material/weather-night",
                "name": "Cambiar al modo claro",
            },
        },
    ],
    # BEGIN: version_dropdown
    # "version_dropdown": True,
    # "version_info": [
    #     {
    #         "version": "https://entrenamiento-python-avanzado.readthedocs.io/es/3/",
    #         "title": "3",
    #         "aliases": [],
    #     },
    # ],
    # END: version_dropdown
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project_details

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = project_short_name[0].capitalize() + project_short_name[1:53]

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/python_logo_web.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = '_static/favicon/favicon-16x16.png'
html_favicon = "_static/favicon.png"

# A list of CSS files. The entry must be a filename string or a tuple containing
# the filename string and the attributes dictionary. The filename must be relative
# to the html_static_path, or a full URI with scheme like https://example.org/style.css.
# The attributes is used for attributes of <link> tag. It defaults to an empty list.
html_css_files = [
    "https://netdna.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
    "stylesheets/virtual_business_card.css",
    "stylesheets/soporte_profesional.css",
    "stylesheets/sphinx_contributors.css",
    "stylesheets/main/layout/_content.css",
    "stylesheets/main/layout/_footer.css",
]

# A list of JavaScript filename. The entry must be a filename string or a tuple containing
# the filename string and the attributes dictionary. The filename must be relative to the
# html_static_path, or a full URI with scheme like https://example.org/script.js.
# The attributes is used for attributes of <script> tag. It defaults to an empty list.
html_js_files = [
    "https://code.jquery.com/jquery-latest.min.js",
    "javascripts/virtual_business_card.js",
    "javascripts/real_time.js",
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
html_extra_path = [
    "_templates/browserconfig.xml",
    "_templates/manifest.json",
    "_templates/robots.txt",
]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%d de %B de %Y"

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# Suffix to be appended to source links (see html_show_sourcelink), unless
# they have this suffix already. Default is '.txt'.
html_sourcelink_suffix = ".rst"

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
html_use_opensearch = "entrenamiento-python-avanzado.readthedocs.io"


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = f"{project_name}doc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    "papersize": "a4paper",
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # "inputenc" package inclusion, default '\\usepackage[utf8]{inputenc}'.
    "inputenc": r"""
    \usepackage[utf8]{inputenc}
    """,
    # "fontenc" package inclusion, default '\\usepackage[T1]{fontenc}'.
    # 'fontenc': r'''
    # \usepackage[T1]{fontenc}
    # ''',
    # Additional stuff for the LaTeX preamble.
    #
    "preamble": r"""
    \usepackage{pmboxdraw}
    \authoraddress{
      \strong{Contactos:} \email{leonardocaballero@gmail.com} -
      \url{https://github.com/macagua}\\
      \strong{Ciudad de Mérida, Estado Mérida, Venezuela. 5101.}\\
      \strong{Telf.} +58-412-473.53.76 (WhatsApp / Telegram)
    }
    \let\Verbatim=\OriginalVerbatim
    \let\endVerbatim=\endOriginalVerbatim
    """,
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    # Additional footer content (before the indices), default empty.
    # 'footer': 'Ing. Leonardo J. Caballero G.'
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (root_doc, project_name + ".tex", project_details, author, "manual"),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "_static/python_logo_print.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
latex_show_pagerefs = True

# If true, show URL addresses after external links.
latex_show_urls = "footnote"

# Documents to append as an appendix to all manuals.
latex_appendices = [
    "acerca_de",
    "esquema",
    "lecturas",
    "glosario",
    "copyright",
    "licencia",
]

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        root_doc,
        project_name,
        project_details,
        author,
        project_name,
        project_details,
        "Misceláneos",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = ['apendices/operadores', 'glosario','licencia']

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project_details
epub_author = author
epub_publisher = publisher
epub_copyright = f"{years}, {author}"

# The language of the text. It defaults to the language option
# or 'en' if the language is not set.
epub_language = language

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#
# epub_cover = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#
# epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#
# epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# The depth of the table of contents in toc.ncx.
#
# epub_tocdepth = 3

# Allow duplicate toc entries.
#
# epub_tocdup = True


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
# Add mappings
# https://kev.inburke.com/kevin/sphinx-interlinks/
intersphinx_mapping = {
    "python3": ("https://docs.python.org/3.11/", None),
    "entrenamiento-python-basico": ("https://entrenamiento-python-basico.readthedocs.io/es/3.7/", None),
    "entrenamiento-frameworks-web-python": ("https://entrenamiento-frameworks-web-python.readthedocs.io/es/latest/", None),
}
intersphinx_timeout = 120

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# If true, ....
todo_emit_warnings = False

# -- Options for sphinx-tabs extension -------------------------------

# If needed, allow additional builders to be considered compatible.
sphinx_tabs_valid_builders = ["linkcheck"]

# Disable the tabs can be closed by selecting the open tab, by default
sphinx_tabs_disabled_tab_closing = True

# -- Options for sphinxcontrib-email extension -------------------------------

# Set True to automatically obfuscate all mailto links.
email_automode = True

# -- Options for quizdown extension ------------------------------------------

# Global options passed to the quizdown library
quizdown_config = {
    # quizdown javascript
    "quizdown_js": "https://cdn.jsdelivr.net/gh/bonartm/quizdown-js@latest/public/build/quizdown.js",
    # detect and convert all divs with class quizdown
    "start_on_load": True,
    # shuffle answers for each question
    "shuffle_answers": True,
    # shuffle questions for each quiz
    "shuffle_questions": True,
    # primary CSS color
    "primary_color": "#FF851B",
    # secondary CSS color
    "secondary_color": "#DDDDDD",
    # text color of interactive elements
    "text_color": "black",
    # language of text in user interface
    "locale": "es",
}

# -- Options for yasfb extension ---------------------------------------------

# Set the Feed Base Url.
feed_base_url = "https://entrenamiento-python-avanzado.readthedocs.io/es/latest/"

# Set the Feed Author Name.
feed_author = "Leonardo Caballero"

# -- Options for disqus extension --------------------------------------------

# Set disqus site short name.
disqus_shortname = "frameworks-de-desarrollo-web-en-python"

# -- Options for main setup --------------------------------------------------

# def setup(app):
#     from sphinx.util.texescape import tex_replacements
#    print(tex_replacements)
#    tex_replacements.append((u"’", u"'"))
#    tex_replacements.remove((u"’", r"'"))
#    tex_replacements.remove(('─', r'-'))
#    tex_replacements.remove(('│', r'\textbar{}'))