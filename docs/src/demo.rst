Demo
====

This is used to demonstrate various features, and also for testing.

-------------------------------------------------------------------------------

Autodoc
-------

.. currentmodule:: piccolo_theme.snippets

.. autoclass:: Column

-------------------------------------------------------------------------------

Breathe
-------

.. doxygenclass:: CppClass
    :members:

.. doxygenfunction:: cpp_function

.. doxygenfunction:: c_function
    :project: c_demo

-------------------------------------------------------------------------------

Code Blocks
-----------

Basic
~~~~~

.. code-block:: python

  def say_hello():
      print("hello world!")

Emphasize
~~~~~~~~~

.. code-block:: python
  :emphasize-lines: 1,2

  def say_hello():
      print("hello world!")

-------------------------------------------------------------------------------

Tables
------

Table 1
~~~~~~~

====== =======
Name   Drives
====== =======
Alice  True
Bob    True
Curtis False
====== =======

Table 2
~~~~~~~

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
|            |                        |
|            | And several paragraphs.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

-------------------------------------------------------------------------------

Data definitions
----------------

Python
  A great programming language.

Sphinx
  A powerful documentation tool.

-------------------------------------------------------------------------------

Lists
-----

Unordered List
~~~~~~~~~~~~~~

* Python
* Rust
* Javascript

Ordered List
~~~~~~~~~~~~

1. Python
2. Rust
3. Javascript

-------------------------------------------------------------------------------

Admonitions
-----------

.. warning:: This is a warning!

.. error:: This is an error!

.. hint:: This is a hint!

.. note:: This is a note!

.. admonition:: A custom admonition

   This is my custom admonition!
