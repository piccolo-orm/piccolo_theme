import os
import typing as t

from sphinx.application import Sphinx


def setup(app: Sphinx):
    """
    :param app:
        Passed by Sphinx.

    """
    app.add_html_theme(
        "piccolo_theme", os.path.abspath(os.path.dirname(__file__))
    )
