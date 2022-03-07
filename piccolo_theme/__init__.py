import os

from sphinx.application import Sphinx


__VERSION__ = "0.5.0"


def setup(app: Sphinx):
    """
    :param app:
        Passed by Sphinx.

    """
    app.add_html_theme(
        "piccolo_theme", os.path.abspath(os.path.dirname(__file__))
    )
