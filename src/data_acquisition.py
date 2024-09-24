# src/data_acquisition.py

import requests
import streamlit as st

API_KEY = st.secrets.get("API_KEY")
if not API_KEY:
    st.error("API_KEY not found. Please set it in Streamlit Secrets.")
    st.stop()

def get_solunar_data(lat, lon, date):
    url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
    date_str = date.strftime('%Y-%m-%d')
    params = {
        'key': API_KEY,
        'include': 'hours',
        'elements': 'datetime,sunrise,sunset,moonphase,moonrise,moonset',
    }
    response = requests.get(f"{url}{lat},{lon}/{date_str}", params=params)
    if response.status_code == 200:
        try:
            data = response.json()
            return data
        except requests.exceptions.JSONDecodeError:
            st.error("Failed to parse JSON response from the API.")
            st.write("Response content:", response.text)
            return None
    else:
        st.error(f"Error fetching data: {response.status_code} - {response.reason}")
        st.write("Response content:", response.text)
        return None
