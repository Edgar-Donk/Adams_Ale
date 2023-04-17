import altair as alt
import numpy as np
import pandas as pd

T = np.linspace(0, 30, 31)

hfg = 2500.304 - 2.2521025 * T - 0.02146547 * np.power(T, 1.5) + \
    3.1750136e-04 * np.power(T, 2.5) - 2.8607959e-05 * np.power(T, 3)

source = pd.DataFrame({
  'T': T,
  'hfg': hfg
})

chart = alt.Chart(source).mark_line().encode(
    x=alt.X('T', axis=alt.Axis(title='Temperature °C')),
    y=alt.Y('hfg', axis=alt.Axis(title='Latent Heat kJ/kg'),
           scale=alt.Scale(domain=(2420, 2510))
           ),
    tooltip=['T', alt.Tooltip('hfg', format='.1f')]
).properties(
        title={
            "text": "Latent Heat Evaporisation of Water",
            "color": "#282828"
        }
    )

chart.save('lat_heat.html')
