import altair as alt
from vega_datasets import data
source = data.cars()
base = alt.Chart(source).mark_point().encode(
    x='Horsepower:Q',
      y='Miles_per_Gallon:Q',
   ).properties(
      width=140,
      height=140
   )
alt.hconcat(
      base.encode(color='Cylinders:Q').properties(title='quantitative'),
      base.encode(color='Cylinders:O').properties(title='ordinal'),
      base.encode(color='Cylinders:N').properties(title='nominal'),
   )

base.save('plot-datatypes.html')