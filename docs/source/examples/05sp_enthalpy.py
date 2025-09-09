import altair as alt
import numpy as np
import pandas as pd

T = np.linspace(0, 30, 31)

hs = -2.844699e-02 + 4.211925 * T - 1.017034e-03 * np.power(T, 2) + \
    1.311054e-05 * np.power(T, 3) - 6.756469e-08 * np.power(T, 4) + \
    1.724481e-10 * np.power(T, 5)

source = pd.DataFrame({
  'Temperature °C': T,
  'Specific Enthalpy of Liquid Water': hs
})

chart = alt.Chart(source).mark_line().encode(
    x=alt.X('Temperature °C', axis=alt.Axis(title='Temperature °C')),
    y=alt.Y('Specific Enthalpy of Liquid Water', axis=alt.Axis(title='Spec Enthalpy kJ/kg')),
    tooltip=['Temperature °C', alt.Tooltip('Specific Enthalpy of Liquid Water', format='.2f')]
).properties(
        title={
            "text": "Specific Enthalpy of Liquid Water",
            "color": "#282828"
        }
    )

chart.save('sp_enthalpy.html')