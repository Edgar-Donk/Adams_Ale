======================
Specific Volume Vapour 
======================

.. raw:: html
    :file: ../examples/spvol_vap.html

The simplified equation comes from Wagner and Pruss.

.. math::

    ϴ_{sv} = (\frac{1}{ρ_c})\cdot exp(c_1\cdot τ^{1/3} + c_2\cdot τ^{2/3}
        + c_3\cdot τ^{4/3} + c_4\cdot τ^3 + c_5\cdot τ^{37/6} + c_6\cdot τ^{71/6}) \tag{4}

.. |pc| replace:: ρ\ :sub:`c`\
.. |Tsv| replace:: ϴ\ :sub:`sv`\
.. |c1| replace:: c\ :sub:`1`\
.. |c2| replace:: c\ :sub:`2`\
.. |c3| replace:: c\ :sub:`3`\
.. |c4| replace:: c\ :sub:`4`\
.. |c5| replace:: c\ :sub:`5`\
.. |c6| replace:: c\ :sub:`6`\
.. |Tc| replace:: T\ :sub:`c`\

where

    ===== =================================================
    Var         Description
    ===== =================================================
    |Tsv|   is saturated vapour specific volume, m³/kg
    |pc|    is critical density of water, 322 m³/kg
    |Tc|    is the critical temperature water, 647.096 K
    T       is temperature of the water °C
    τ       is the reduced temperature, 1-(273.15+T)/|Tc|
    |c1|    is 2.03150240
    |c2|    is 2.68302940
    |c3|    is 5.38626492
    |c4|    is 17.2991605
    |c5|    is 44.7586581
    |c6|    is 63.9201063
    ===== =================================================

.. container:: toggle

    .. container:: header

        *Show/Hide Code* 04spvol_vap.py

    .. literalinclude:: ../examples/04spvol_vap.py
