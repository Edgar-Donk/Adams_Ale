import altair as alt
import numpy as np
import pandas as pd
#alt.renderers.enable('altair_viewer')

T = np.linspace(0, 30, 31)
tau = 1 - (273.15 + T)/647.096

expo = 2.03150240 * np.power(tau, 1/3) + 2.68302940 * np.power(tau, 2/3) + \
        5.38626492 * np.power(tau, 4/3) + 17.2991605 * np.power(tau, 3) + \
        44.7586581 * np.power(tau, 37/6) + 63.9201063 * np.power(tau, 71/6)

th = 1/322 * np.exp(expo)

source = pd.DataFrame({
  'Temperature °C': T,
  'sat vap sp volume, m³/kg': th
})

chart = alt.Chart(source).mark_line().encode(
    x=alt.X('Temperature °C', axis=alt.Axis(title='Temperature °C')),
    y=alt.Y('sat vap sp volume, m³/kg',
           scale=alt.Scale(domain=(30, 210)),
            axis=alt.Axis(title='sat vap sp volume, m³/kg')),
    tooltip=['Temperature °C', alt.Tooltip('sat vap sp volume, m³/kg', format='.2f')]
).properties(
        title={
            "text": "Saturated Vapour Specific Volume",
            "color": "#282828"
        }
    )

chart.save('spvol_vap.html')
#chart.show()