import altair as alt
import numpy as np
import pandas as pd

T = np.linspace(0, 30, 31)

pr = 1 / (0.074763403 + 0.0029020983 * T + 2.8606181e-05 * np.power(T, 2) - \
    8.1395537e-08 * np.power(T, 3))

source = pd.DataFrame({
  'T': T,
  'pr': pr
})

chart = alt.Chart(source).mark_line().encode(
    x=alt.X('T', axis=alt.Axis(title='Temperature °C')),
    y=alt.Y('pr', axis=alt.Axis(title='Prandtl Number'),
           scale=alt.Scale(domain=(5, 14))
           ),
    tooltip=['T', alt.Tooltip('pr', format='.2f')]
).properties(
        title={
            "text": "Prandtl Number of Saturated Liquid Water",
            "color": "#282828"
        }
    )

chart.save('prandtl.html')
