import altair as alt
import numpy as np
import pandas as pd

T = np.linspace(0, 30, 31)

sig = 0.075652711 - 0.00013936956 * T - 3.0842103e-07 * np.power(T, 2) + \
    2.7588435e-10 * np.power(T, 3)

source = pd.DataFrame({
  'Temperature °C': T,
  'Surface Tension N/m': sig
})

chart = alt.Chart(source).mark_line().encode(
    x=alt.X('Temperature °C', axis=alt.Axis(title='Temperature °C')),
    y=alt.Y('Surface Tension N/m', axis=alt.Axis(title='Surface Tension N/m'),
           scale=alt.Scale(domain=(0.0710, 0.0760))
           ),
    tooltip=['Temperature °C', alt.Tooltip('Surface Tension N/m', format='.5f')]
).properties(
        title={
            "text": "Surface Tension of Saturated Liquid Water",
            "color": "#282828"
        }
    )

chart.save('surf_tens.html')