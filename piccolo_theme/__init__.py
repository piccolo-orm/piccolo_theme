import os
import typing as t

if t.TYPE_CHECKING:
    from sphinx.application import Sphinx


__VERSION__ = "0.11.1"


def setup(app: 'Sphinx'):
    """
    :param app:
        Passed by Sphinx.

    """

    app.add_html_theme(
        "piccolo_theme", os.path.abspath(os.path.dirname(__file__))
    )

    ###########################################################################
    # Try and infer which Git icon to use based on the URL:

    html_theme_options = getattr(app.config, 'html_theme_options')

    if html_theme_options:
        if isinstance(html_theme_options, dict):
            git_url = html_theme_options.get('git_url')
            git_icon = html_theme_options.get('git_icon')
            if isinstance(git_url, str) and not git_icon:
                if 'github.com' in git_url:
                    html_theme_options['git_icon'] = 'github'
                elif 'gitlab.com' in git_url:
                    html_theme_options['git_icon'] = 'gitlab'
                else:
                    html_theme_options['git_icon'] = 'git'
