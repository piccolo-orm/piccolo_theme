Contributing
============

We use `Sass <https://sass-lang.com/>`_ as a CSS preprocessor. The styles live
in ``src/sass``.

To modify the styles, first install SASS:

.. code-block:: bash

    npm install -g sass

Then run:

.. code-block:: bash

    ./scripts/build-styles.sh

This will automatically rebuild your CSS when it detects a change in the
SASS files.
