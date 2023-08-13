import streamlit as st
import pandas as pd
import numpy as np
import plost
from PIL import Image

# Page setting
st.set_page_config(layout="wide")

# mostrar el directorio de trabajo con python


with open('./pages/resources/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Data
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

# Row A
a1, a2, a3 = st.columns(3)
a1.image(Image.open('./pages/resources/streamlit-logo-secondary-colormark-darktext.png'))
a2.metric("Viento", "1.2 kph", "-8%")
a3.metric("Humedad", "86%", "4%")

# Row B
b1, b2, b3, b4 = st.columns(4)
b1.metric("Temperatura", "27 °C", "0.3 °C")
b2.metric("Viento", "0.7 mph", "-8%")
b3.metric("Humedad", "86%", "4%")
b4.metric("Humedad", "86%", "4%")

# Row C
c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap')
    plost.time_hist(
    data=seattle_weather,
    date='date',
    x_unit='week',
    y_unit='day',
    color='temp_max',
    aggregate='median',
    legend=None)
with c2:
    st.markdown('### Bar chart')
    plost.donut_chart(
        data=stocks,
        theta='q2',
        color='company')