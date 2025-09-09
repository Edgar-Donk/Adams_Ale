===========
Latent Heat
===========

.. raw:: html
    :file: ../examples/lat_heat.html

The latent heat of vapourisation was calculated with the equation,

.. math::

    h_{fg} = h_{sv} - h_s

to create the approximate formula,

.. math::

    h_{fg} = a + b\cdot T + c\cdot T^{1.5} + d\cdot T^{2.5} + e\cdot T^3 \tag{7}

.. |hfg| replace:: h\ :sub:`fg`\
.. |hsv| replace:: h\ :sub:`sv`\
.. |hs| replace:: h\ :sub:`s`\

where

    ===== =================================================
    Var         Description
    ===== =================================================
    |hfg|   is the latent heat liquid water, kJ/kg
    |hsv|   is the enthalpy of the vapour, kJ*K
    |hs|   is the enthalpy of the liquid, kJ*K
    T       is temperature of the water °C
    a       is 2500.304
    b       is -2.2521025
    c       is -0.02146547
    d       is 3.1750136e-04
    e       is -2.8607959e-05
    ===== =================================================

.. raw:: html

   <details>
   <summary style="color:MediumSlateBlue"> 
   <i> Show/Hide Code </i> 07lat_ht.py </summary>

.. literalinclude:: ../examples/07lat_ht.py

.. raw:: html

   </details>

|