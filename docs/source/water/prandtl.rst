==============
Prandtl Number
==============

.. raw:: html
    :file: ../examples/prandtl.html

.. math::

    Pr_s = \frac {1}{a + b\cdot T + c\cdot T^2 + d\cdot T^3} \tag{10}

.. |pr| replace:: Pr\ :sub:`s`\

where

    ===== ==================================================
    Var         Description
    ===== ==================================================
    |Pr|    is the Prandtl number liquid water
    T       is temperature of the water °C
    a       is 0.074763403
    b       is 0.0029020983
    c       is 2.8606181e-05
    d       is -8.1395537e-08
    ===== ==================================================

   <details>
   <summary style="color:MediumSlateBlue"> 
   <i> Show/Hide Code </i> 10prandtl.py </summary>

.. literalinclude:: ../examples/10prandtl.py

.. raw:: html

   </details>

|