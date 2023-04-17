# Python3 program to illustrate
# How to do custom mapping
# of colors to discrete values
# for scatter plot coloring
# using altair

# Importing altair and vega_datasets library
import altair as alt
from vega_datasets import data

# Selecting the cars dataset
cars = data.cars()

# Making two lists for
# values and colors resp.
dom = ['Europe', 'Japan', 'USA']
rng = ['red', 'green', 'black']

# Making the Scatter Plot
alt.Chart(cars).mark_point().encode(

	# Map Miles_per_Gallon to x-axis
	x='Miles_per_Gallon',

	# Map the Horsepower to y-axis
	y='Horsepower',

	# Coloring the Scatter Plot
	# using Origin variable and
	# custom colors
	color=alt.Color('Origin', scale=alt.
					Scale(domain=dom, range=rng)) # Scale(scheme = 'dark2')
)
