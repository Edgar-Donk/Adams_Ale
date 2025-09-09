====================
Thermal Conductivity
====================

.. raw:: html
    :file: ../examples/th_condy.html

The simplified equation from Sengers and Watson is used.

.. math::

    λ_s = a + b\cdot T + c\cdot T^{1.5} + d\cdot T^2 + e\cdot T^{0.5} \tag{8}

.. |ls| replace:: λ\ :sub:`s`\

where

    ===== ===================================================
    Var         Description
    ===== ===================================================
    |ls|    is the thermal conductivity liquid water, W/(m K)
    T       is temperature of the water °C
    a       is 0.5650285
    b       is 0.0026363895
    c       is -0.00012516934
    d       is -1.5154918e-06
    e       is -0.0009412945
    ===== ===================================================

.. raw:: html

   <details>
   <summary style="color:MediumSlateBlue"> 
   <i> Show/Hide Code </i> 08th_condy.py </summary>

.. literalinclude:: ../examples/08th_condy.py

.. raw:: html

   </details>

|    
