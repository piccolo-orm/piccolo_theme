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
