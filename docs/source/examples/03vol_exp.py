import altair as alt
import numpy as np
import pandas as pd

T = np.linspace(0, 30, 31)

b = -6.8785895e-05 + 2.1687942e-05 * T - 2.1236686e-06 * np.power(T, 1.5) + \
    7.7200882e-08 * np.power(T,2)

source = pd.DataFrame({
  'T': T,
  'b': b
})

chart = alt.Chart(source).mark_line().encode(
    x=alt.X('T', axis=alt.Axis(title='Temperature °C')),
    y=alt.Y('b', axis=alt.Axis(title='Coefft Vol Thermal Expn 1/K')),
    tooltip=['T', alt.Tooltip('b', format='.5f')]
).properties(
        title={
            "text": "Coefficient Volumetric Thermal Expansion of Liquid Water"
        }
    )

chart.save('Vol_expn.html')