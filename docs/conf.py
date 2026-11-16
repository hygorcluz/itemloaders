project = "itemloaders"
project_copyright = "Zyte Group Ltd"

extensions = [
    "sphinx.ext.coverage",
    "sphinx_scrapy",
]

exclude_patterns = ["build"]

pygments_style = "sphinx"

html_theme = "sphinx_rtd_theme"
html_last_updated_fmt = "%b %d, %Y"

nitpicky = True
nitpick_ignore = [("py:class", "itemloaders._StatsCollector")]

scrapy_intersphinx_enable = ["parsel"]


def setup(app):
    app.connect("autodoc-skip-member", maybe_skip_member)


def maybe_skip_member(app, what, name, obj, skip, options):
    if not skip:
        # autodocs was generating a text "alias of" for the following members
        # https://github.com/sphinx-doc/sphinx/issues/4422
        return name == "default_item_class"
    return skip
