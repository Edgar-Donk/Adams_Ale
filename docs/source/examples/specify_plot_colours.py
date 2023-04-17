import altair as alt
from vega_datasets import data

source = data.movies()

colors = ['#7fc97f','#beaed4','#fdc086']

alt.Chart(source).mark_line().encode(
    x=alt.X("IMDB_Rating", bin=True),
    y=alt.Y(
        alt.repeat("layer"), aggregate="mean", title="Mean of US and Worldwide Gross"
    ),
    color=alt.datum(alt.repeat("layer")),
).repeat(
    layer=["US_Gross", "Worldwide_Gross", "Production_Budget"],
).configure_range(
    category=alt.RangeScheme(colors)
)