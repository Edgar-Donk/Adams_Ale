import altair as alt
import numpy as np
import pandas as pd

T = np.linspace(0, 30, 31)

ls = 0.5650285 + 0.0026363895 * T - 0.00012516934 * np.power(T, 1.5) - \
    1.5154918e-06 * np.power(T, 2) - 0.0009412945 * np.power(T, 0.5)

source = pd.DataFrame({
  'T': T,
  'ls': ls
})

chart = alt.Chart(source).mark_line().encode(
    x=alt.X('T', axis=alt.Axis(title='Temperature °C')),
    y=alt.Y('ls', axis=alt.Axis(title='Thermal condy W/(m K)'),
           scale=alt.Scale(domain=(0.56, 0.62))
           ),
    tooltip=['T', alt.Tooltip('ls', format='.1f')]
).properties(
        title={
            "text": "Thermal Conductivity of Saturated Liquid Water",
            "color": "#282828"
        }
    )

chart.save('th_condy.html')
