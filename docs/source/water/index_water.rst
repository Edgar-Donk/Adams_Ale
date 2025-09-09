=====
Water
=====

The paper published by C.O.Popiel and J.Wojtkowiak has been extensively
used in this web site. 

Each of the pages show the simplified equations, which are visualised. As
these are simple lineplots any of the python plotting libraries can be used.

Altair is being used, the graphs are interactive and show the x, y values 
where the temperature value is a whole number, and the user's mouse hovers 
over the plot. This property is scripted using the *tooltip* method. The 
formula is first loaded into a pandas DataFrame from which altair reads into
a line plot. Title and axis label names have been added. Where needed the y-axis
has a *scale* added so that the plot displays over the required temperature 
range 0 to 30°C.

If further information is required about plotting then read up 
:ref:`Visualisation<vis>`.

.. toctree::
   :maxdepth: 3
   :caption: Properties:
   
   satpress
   density
   volumetric
   spvol_vap
   spenthalpy
   spheat
   latheat
   thcondy
   dynviscy
   prandtl
   surftens