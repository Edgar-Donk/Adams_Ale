=================
Dynamic Viscosity
=================

.. raw:: html
    :file: ../examples/dyn_viscy.html

The equation from Sengers and Watson was used to make a simplified equation

.. math::

    μ_s = \frac {10^5}{a + b\cdot T + c\cdot T^2 + d\cdot T^3} \tag{9}

.. |ms| replace:: μ\ :sub:`s`\

where

    ===== ==================================================
    Var         Description
    ===== ==================================================
    |ms|    is the dynamic viscosity liquid water, kg/m s
    T       is temperature of the water °C
    a       is 557.82468
    b       is 19.408782
    c       is 0.1360459
    d       is -3.1160832e-04
    ===== ==================================================

The units for the y axis kg/(m s) have been corrected so that the plot
displays between 800 to 1800 between 0 and 30°C. The basis for this was that
the uncorrected formula plotted between 0.00080 and 0.00180 and the viscosity 
of water at 20°C and 1 bar is :math:`1002.0\cdot 10^{-06}kg/m s`, shown at the 
end of the dynamic viscosity section in the paper by Popiel and Wojtkowiak 
(probably a misprint in my copy). 

.. hint:: 

    Hover your mouse over the intersection between the plot and 20°C, the
    tooltip shows ``1002.1``.

.. raw:: html

   <details>
   <summary style="color:MediumSlateBlue"> 
   <i> Show/Hide Code </i> 09dyn_viscy.py </summary>

.. literalinclude:: ../examples/09dyn_viscy.py

.. raw:: html

   </details>

|