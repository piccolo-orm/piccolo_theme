import os


def setup(app):
    """
    :param app:
        Passed by Sphinx.

    """
    app.add_html_theme(
        "piccolo_theme", os.path.abspath(os.path.dirname(__file__))
    )
