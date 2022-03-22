Configuration
=============

html_short_title
----------------

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

banner_text
~~~~~~~~~~~

If this is provided then a banner is shown at the top of the page. It's useful
for important announcements.

.. code-block:: python

    # conf.py

    html_theme_options = {
        # Note how we can include links:
        "banner_text": 'We just launched a newletter, <a href="https://mynewsletter.com/">please subscribe</a>!'
    }
