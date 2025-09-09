import altair as alt
import numpy as np
import pandas as pd

T = np.linspace(0, 30, 31)

ms = 1e06 / (557.82468 + 19.408782 * T + 0.1360459 * np.power(T, 2) - \
    3.1160832e-04 * np.power(T, 3))

source = pd.DataFrame({
  'Temperature °C': T,
  'Dynamic Viscosity': ms
})

chart = alt.Chart(source).mark_line().encode(
    x=alt.X('Temperature °C', axis=alt.Axis(title='Temperature °C')),
    y=alt.Y('Dynamic Viscosity', axis=alt.Axis(title='Dynamic Viscosity  x 1e-06 kg/(m s)'),
           scale=alt.Scale(domain=(800, 1800))
           ),
    tooltip=['Temperature °C', alt.Tooltip('Dynamic Viscosity', format='.1f')]
).properties(
        title={
            "text": "Dynamic Viscosity of Saturated Liquid Water",
            "color": "#282828"
        }
    )

chart.save('dyn_viscy.html')
