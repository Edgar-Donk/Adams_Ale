=================
Specific Enthalpy
=================

.. raw:: html
    :file: ../examples/sp_enthalpy.html

A simplified equation by Kostyrko and Pluciennik is used for the specific
enthalpy of saturated water.

.. math::

    h_s = d_1 + d_2\cdot T + d_3\cdot T^2 + d_4\cdot T^3 + d_5\cdot T^4 + d_6\cdot T^5 \tag{5}

.. |hs| replace:: h\ :sub:`s`\
.. |d1| replace:: d\ :sub:`1`\
.. |d2| replace:: d\ :sub:`2`\
.. |d3| replace:: d\ :sub:`3`\
.. |d4| replace:: d\ :sub:`4`\
.. |d5| replace:: d\ :sub:`5`\
.. |d6| replace:: d\ :sub:`6`\

where

    ==== ===============================================================
    Var         Description
    ==== ===============================================================
    |hs|    is the specific enthalpy water, kJ/kg
    T       is temperature of the water °C
    |d1|    is -2.844699e-02
    |d2|    is 4.211925
    |d3|    is -1.017034e-03
    |d4|    is 1.311054e-05
    |d5|    is -6.756469e-08
    |d6|    is 1.724481e-10
    ==== ===============================================================

which should give an almost linear plot.

.. container:: toggle

    .. container:: header

        *Show/Hide Code* 05sp_enthalpy.py

    .. literalinclude:: ../examples/05sp_enthalpy.py