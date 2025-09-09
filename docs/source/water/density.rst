==============
Liquid Density
==============

.. raw:: html
    :file: ../examples/Density_water_title_red.html

Liquid density has a simplified equation valid in the temperature range 0 to
150°C. Once again the range is shown only for 0 to 30°C.

.. math::

    ρ_s = a + b\cdot T + c\cdot T^2 +d\cdot T^{2.5} + e\cdot T^3  \tag{2}

.. |ps| replace:: ρ\ :sub:`s`\

where

    ===== =================================================
    Var         Description
    ===== =================================================
    |ps|    is the density of liquid water, kg/m³
    T       is temperature of the water °C
    a       is 999.79684
    b       is 0.068317355
    c       is -0.010740248
    d       is 0.00082140905
    e       is -2.3030988e-05
    ===== =================================================
    
The plot shows the maximum at the point of maximum density.

.. raw:: html

   <details>
   <summary style="color:MediumSlateBlue"> 
   <i> Show/Hide Code </i> 02density_water.py </summary>

.. literalinclude:: ../examples/02density_water.py

.. raw:: html

   </details>

|