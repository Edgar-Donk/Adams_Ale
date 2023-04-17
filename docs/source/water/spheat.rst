=============
Specific Heat
=============

.. raw:: html
    :file: ../examples/Sp_heat.html

Specific heat water at 1 bar.

.. math::

    c_{p,s} = a + b\cdot T + c\cdot T^{1.5} + d\dot T^2 + e\cdot T^{2.5} \tag{6}

.. |cps| replace:: c\ :sub:`p,s`\

where

    ===== =================================================
    Var         Description
    ===== =================================================
    |cps|    is the specific heat liquid water, kJ/(kg K)
    T       is temperature of the water °C
    a       is 4.2174356
    b       is -0.0056181625
    c       is 0.0012992528
    d       is -0.00011535353
    e       is 4.14964e-06
    ===== =================================================

The plot is from 0 to 30°C, but is valid 0 to 130°C. A minimum is at
~35°C.

.. container:: toggle

    .. container:: header

        *Show/Hide Code* 06sp_ht.py

    .. literalinclude:: ../examples/06sp_ht.py