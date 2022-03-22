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

-------------------------------------------------------------------------------

Theme specific
--------------

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
useful when the banner contains information which the user is unlikely to be
needed again. For example:

.. code-block:: python

    # conf.py

    html_theme_options = {
        "banner_text": 'Welcome to our amazing documentation!',
        "banner_hiding": "permanent"
    }

.. note:: If you configure a different ``banner_text`` value in the future,
   then the banner will appear again, even if the user has previously hidden
   it.
