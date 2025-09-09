===================================
Volumetric Thermal Expansion Coefft
===================================

.. raw:: html
    :file: ../examples/Vol_expn.html

Using the definition

.. math::

    ß = \frac{1}{υ_s} \cdot \frac{δυ_s} {δT} = -\frac{1}{ρ_s} \cdot \frac{δρ_s} {δT} \tag{3}

and the density of water equation (2) the volumetric thermal expansion 
coefficient can be calculated with a simplified equation 0-150°C.

.. math::

    ß = a + b \cdot T + c \cdot T^{1.5} + d \cdot T^2

where

    ===== =================================================
    Var         Description
    ===== =================================================
    ß       is the coefft volumetric thermal expansion, 1/K
    T       is temperature of the water °C
    a       is -6.8785895e-05
    b       is 2.1687942e-05
    c       is -2.1236686e-06
    d       is 7.7200882e-08
    ===== =================================================

At the temperature of maximum density the coefficient of volumetric thermal
expansion is zero as the values pass from positive to negative values.

.. raw:: html

   <details>
   <summary style="color:MediumSlateBlue"> 
   <i> Show/Hide Code </i> 03vol_exp.py </summary>

.. literalinclude:: ../examples/03vol_exp.py

.. raw:: html

   </details>

|