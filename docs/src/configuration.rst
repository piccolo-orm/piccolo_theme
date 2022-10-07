Configuration
=============

``html_short_title``
--------------------

If you have a really long project name, you may prefer something shorter to
appear in the navigation bar. Specify this using ``html_short_title`` in
``conf.py``:

.. code-block:: python

    # conf.py

    # By default the project value is used in the nav bar.
    project = 'My Extra Special Amazing Docs'

    # If specified, this will be used in the nav bar instead.
    html_short_title = "Amazing Docs"

``html_logo``
-------------

If you prefer an image logo to a text in the nav bar, specify this using 
``html_logo`` in ``conf.py``:

.. code-block:: python

    # If specified, this will be used in the nav bar instead of textual title
    html_logo = './_static/logo.png'

.. note:: It is a common practice to place static resources like images
   inside of subdirectories (e.g. ``_static``). Make sure to list such a 
   directory in the variable ``html_static_path = []``.

-------------------------------------------------------------------------------

Theme specific
--------------

``source_url``
~~~~~~~~~~~~~~

If specified, a link is shown in the nav bar to the source code.

.. code-block:: python

    # conf.py

    html_theme_options = {
        "source_url": 'https://github.com/piccolo-orm/piccolo_theme/'
    }

We try and detect if the URL points to GitHub or GitLab, and show the correct
icon. However, if you're using a self hosted version of GitHub or GitLab on a
custom URL, you can explicitly tell the theme which icon to use:

.. code-block:: python

    # conf.py

    html_theme_options = {
        "source_url": 'https://self-hosted.foo.com/',
        "source_icon": "gitlab"
    }

The available options for ``source_icon`` are:

* generic
* github
* gitlab

``banner_text``
~~~~~~~~~~~~~~~

If this is provided then a banner is shown at the top of the page. It's useful
for important announcements.

.. code-block:: python

    # conf.py

    html_theme_options = {
        # Note how we can include links:
        "banner_text": 'We just launched a newletter, <a href="https://mynewsletter.com/">please subscribe</a>!'
    }


``banner_hiding``
~~~~~~~~~~~~~~~~~

This controls how the banner behaves when hidden. The options are
``'temporary'`` (the default) or ``'permanent'``.

If ``'temporary'``, when a user hides the banner they can still reopen it again.
This is useful if you want to store important information in the banner, which
the user may need to refer to again. For example:

.. code-block:: python

    # conf.py

    html_theme_options = {
        "banner_text": 'Please be aware of security issue XYZ!',
        "banner_hiding": "temporary"
    }

If ``'permanent'``, when a user hides the banner it disappears permanently. This is
useful when the banner contains information which the user is unlikely to
need again. For example:

.. code-block:: python

    # conf.py

    html_theme_options = {
        "banner_text": 'Welcome to our amazing documentation!',
        "banner_hiding": "permanent"
    }

.. note:: If you configure a different ``banner_text`` value in the future,
   then the banner will appear again, even if the user has previously hidden
   it.

``show_theme_credit``
~~~~~~~~~~~~~~~~~~~~~

At the bottom of the page is a very small link which says ``Styled using the Piccolo Theme``.

This helps grow awareness of the project, and attract new contributors.

You can hide this if required:

.. code-block:: python

    # conf.py

    html_theme_options = {
        "show_theme_credit": False
    }

If hiding it, please consider :ref:`supporting us <SupportUs>` in a different way.
