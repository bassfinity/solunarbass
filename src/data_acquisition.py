import os
import requests
import streamlit as st

def get_api_key():
    # First, try to get the API_KEY from st.secrets
    try:
        api_key = st.secrets["API_KEY"]
        if api_key:
            return api_key
    except (AttributeError, FileNotFoundError, KeyError):
        pass

    # Next, try to get it from environment variables
    api_key = os.getenv("API_KEY")
    if api_key:
        return api_key

    # Optionally, try to get it from a local config.toml file
    try:
        import toml
        config = toml.load("config.toml")
        api_key = config.get("API_KEY")
        if api_key:
            return api_key
    except (FileNotFoundError, ModuleNotFoundError):
        pass

    # If all else fails, display an error and stop the app
    st.error("API_KEY not found. Please set it in Streamlit Secrets, as an environment variable, or in config.toml.")
    st.stop()

API_KEY = get_api_key()

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
