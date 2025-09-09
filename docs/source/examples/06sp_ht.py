import altair as alt
import numpy as np
import pandas as pd

T = np.linspace(0, 30, 31)

cp = 4.2174356 - 0.0056181625 * T + 0.0012992528 * np.power(T, 1.5) - \
    0.00011535353 * np.power(T, 2) + 4.14964e-06 * np.power(T, 2.5)

source = pd.DataFrame({
  'Temperature °C': T,
  'Sp Heat kJ/(kg K)': cp
})

chart = alt.Chart(source).mark_line().encode(
    x=alt.X('Temperature °C', axis=alt.Axis(title='Temperature °C')),
    y=alt.Y('Sp Heat kJ/(kg K)', axis=alt.Axis(title='Sp Heat kJ/(kg K)'),
           scale=alt.Scale(domain=(4.17, 4.22))),
    tooltip=['Temperature °C', alt.Tooltip('Sp Heat kJ/(kg K)', format='.5f')]
).properties(
        title={
            "text": "Specific Heat at constant pressure of Liquid Water",
            "color": "#282828"
        }
    )

chart.save('Sp_heat.html')
