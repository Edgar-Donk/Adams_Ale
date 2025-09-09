===================
Saturation Pressure
===================

.. raw:: html
    :file: ../examples/Sat_Press_water_title_red.html

The water saturation pressure is the one instance where no simplified
equation is offered.

.. math::

    p_s = p_c exp\{[T_c / (273.15 + T)](a_1 \tau + a_2 \tau ^{1.5} 
            +a_3 \tau ^3 + a_4 \tau ^{3.5} + a_5 \tau ^4 + a_6 \tau ^{7.5})\} \tag{1}

.. |ps| replace:: p\ :sub:`s`\
.. |pc| replace:: p\ :sub:`c`\
.. |Tc| replace:: T\ :sub:`c`\
.. |a1| replace:: a\ :sub:`1`\
.. |a2| replace:: a\ :sub:`2`\
.. |a3| replace:: a\ :sub:`3`\
.. |a4| replace:: a\ :sub:`4`\
.. |a5| replace:: a\ :sub:`5`\
.. |a6| replace:: a\ :sub:`6`\

where

    ==== ===============================================================
    Var         Description
    ==== ===============================================================
    |ps|    is the saturation pressure water, bar 
    |pc|    is the critical pressure water, 220.64 bar
    |Tc|    is the critical temperature water, 647.096 K
    τ       is the reduced temperature, 1-(273.15+T)/|Tc|
    T       is temperature of the water °C
    |a1|    is -7.85951783
    |a2|    is 1.84408259
    |a3|    is -11.7866497
    |a4|    is 22.6807411
    |a5|    is -15.9618719
    |a6|    is 1.80122502
    ==== =============================================================== 

The chart was created by Altair because it was relatively easy to create an
interactive plot to display on the web site. Plotly could have been used
giving a slightly better cursor, if the cursor is not so important then
Seaborn would have made sense. The chart has been created for values between 
0 and 30°C but can be extended to 150°C if required.

In general these plots rely upon numpy to create the data for the x and y
axes.

.. raw:: html

   <details>
   <summary style="color:MediumSlateBlue"> 
   <i> Show/Hide Code </i> 01sat_press_water_title_red.py </summary>

.. literalinclude:: ../examples/01sat_press_water_title_red.py

.. raw:: html

   </details>

|