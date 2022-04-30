from tkinter import font
from turtle import color
import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber Pickups in NYC")

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading the data...')
data = load_data(20000)
data_load_state.text('Loading data (using st.cache)!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
st.markdown(f'<h2 style="color:darkblue;font-size:24px;font-weight:300;text-decoration: underline;font-style: italic;">{"Number Of Pickup By Hours"}</h2>', unsafe_allow_html=True)

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

st.markdown(f'<h2 style="color:darkblue;font-size:24px;font-weight:300;text-decoration: underline;font-style: italic;">{"Map Of All Pickups"}</h2>', unsafe_allow_html=True)

st.map(data)

hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.markdown(f'<h2 style="color:darkblue;font-size:24px;font-weight:300;text-decoration: underline;font-style: italic;">Map of all pickups at {hour_to_filter}:00</h2>', unsafe_allow_html=True)
#st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.markdown(f'<h2 style="color:darkblue;font-size:24px;font-weight:300;text-decoration: underline;font-style: italic;">Map of all pickups at {hour_to_filter}:00</h2>', unsafe_allow_html=True)
st.map(filtered_data)