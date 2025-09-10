import altair as alt
from vega_datasets import data
pop = data.population()

base = alt.Chart(pop).mark_bar().encode(
      alt.Y('mean(people):Q').title('Total population')
   ).properties(
      width=140,
      height=140
   )

alt.hconcat(
      base.encode(x='year:O').properties(title='ordinal'),
      base.encode(x='year:Q').properties(title='quantitative'),
      base.encode(x='year:T').properties(title='temporal')
   )

base.save('plot-datatypes01.html')