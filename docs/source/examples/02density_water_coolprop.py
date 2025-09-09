import altair as alt
import numpy as np
import pandas as pd
from CoolProp.CoolProp import PropsSI

T = np.linspace(0, 30, 31)

ps = 999.79684 + 0.068317355 * T - 0.010740248 * np.power(T, 2) \
    + 0.00082140905 * np.power(T, 2.5) - 2.3030988e-05 * np.power(T, 3)

wds=[PropsSI('D','T',i+273.15,'Q',0,'Water') for i in range(31)]

source = pd.DataFrame({
  'Temperature °C': T,
  'ρs kg/m³': ps,
  'wds': wds
})

source = df.reset_index().melt('x')

chart = alt.Chart(source).mark_line().encode(
    x=alt.X('Temperature °C', axis=alt.Axis(title='Temperature °C')),
    y=alt.Y('ρs kg/m³',
        scale=alt.Scale(domain=(995, 1000)),
        axis=alt.Axis(title='Density kg/m³')
        ),
    tooltip=['Temperature °C', alt.Tooltip('ρs kg/m³', format='.3f')]
).properties(
        title={
            "text": "Density of Liquid Water",
            "color": "red"
        }
    )

chart.save('Density_water_title_red.html')

