import altair as alt
import numpy as np
import pandas as pd

T = np.linspace(0, 30, 31)
tau = 1 - (273.15 + T)/647.096

expo = (-7.85951783*tau+1.84408259*np.power(tau,1.5)-11.7866497*np.power(tau,3)+22.6807411*np.power(tau,3.5)-15.9618719*np.power(tau,4)+1.80122502*np.power(tau,7.5))

pc=220.64*np.exp((647.096/(273.15+T))*expo)

source = pd.DataFrame({
  'Temperature °C': T,
  'Ps bar': pc
})

chart_title = alt.TitleParams(
        "Saturation Pressure of Water")

chart = alt.Chart(source, title=chart_title).mark_line().encode(
    x='Temperature °C',
    y='Ps bar',
    tooltip=['Temperature °C', alt.Tooltip('Ps bar', format='.3f')]
)

chart.save('Sat_Press_water_title.html')