import streamlit as st
from datetime import date, datetime
from streamlit_js_eval import streamlit_js_eval  # For geolocation
from src.data_acquisition import get_solunar_data
from src.data_processing import process_solunar_data
from src.solunar_calculations import calculate_major_minor_times
from src.recommendation_engine import generate_recommendations
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="SolunarBass", page_icon="🎣")

st.title("🎣 SolunarBass")
st.subheader("Optimal Bass Fishing Times Based on Solunar Theory")

# Initialize session state variables
if 'use_current_location' not in st.session_state:
    st.session_state.use_current_location = False
if 'latitude' not in st.session_state:
    st.session_state.latitude = 38.8951
if 'longitude' not in st.session_state:
    st.session_state.longitude = -77.0364
if 'loc' not in st.session_state:
    st.session_state.loc = None
if 'data_fetched' not in st.session_state:
    st.session_state.data_fetched = False
if 'solunar_data' not in st.session_state:
    st.session_state.solunar_data = None
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None

# Sidebar Inputs
st.sidebar.header("Input Parameters")

# Checkbox to use current location
use_current_location = st.sidebar.checkbox("Use my current location", value=st.session_state.use_current_location)
st.session_state.use_current_location = use_current_location

# Button to fetch data
fetch_data = st.sidebar.button("Get Fishing Times")

if st.session_state.use_current_location:
    # Get the user's location using JavaScript
    if st.session_state.loc is None:
        loc = streamlit_js_eval(
            js_expressions="""
            new Promise((resolve, reject) => {
                navigator.geolocation.getCurrentPosition(
                    (position) => {
                        resolve({
                            latitude: position.coords.latitude,
                            longitude: position.coords.longitude
                        });
                    },
                    (error) => {
                        resolve(null);
                    }
                );
            });
            """,
            key="get_location",
        )
        if loc:
            if 'latitude' in loc and 'longitude' in loc:
                st.session_state.latitude = loc["latitude"]
                st.session_state.longitude = loc["longitude"]
                st.session_state.loc = loc
                st.sidebar.success(f"Location acquired: ({st.session_state.latitude:.6f}, {st.session_state.longitude:.6f})")
            else:
                st.sidebar.error("Unable to retrieve location. Please allow location access.")
        else:
            st.sidebar.warning("Waiting for location... Make sure to allow location access.")
else:
    # Manual input
    st.session_state.latitude = st.sidebar.number_input("Latitude", value=st.session_state.latitude, format="%.6f")
    st.session_state.longitude = st.sidebar.number_input("Longitude", value=st.session_state.longitude, format="%.6f")

selected_date = st.sidebar.date_input("Date", value=date.today())

if fetch_data:
    with st.spinner('Fetching data...'):
        raw_data = get_solunar_data(st.session_state.latitude, st.session_state.longitude, selected_date)
        if raw_data is None:
            st.error("Failed to retrieve data. Please try again later.")
        else:
            date_str = selected_date.strftime('%Y-%m-%d')  # Convert date to string
            st.session_state.solunar_data = process_solunar_data(raw_data, date_str)
            major_times, minor_times = calculate_major_minor_times(st.session_state.solunar_data)
            st.session_state.recommendations = generate_recommendations(major_times, minor_times)
            st.session_state.data_fetched = True

# Display Results if Data Has Been Fetched
if st.session_state.data_fetched and st.session_state.solunar_data:
    st.success("Recommendations Generated!")

    # Display Recommendations
    st.header("Recommended Fishing Times")
    for rec in st.session_state.recommendations:
        start_time = rec['start'].strftime('%I:%M %p')
        end_time = rec['end'].strftime('%I:%M %p')
        st.write(f"**{rec['type']} Period:** {start_time} - {end_time}")

    # Display Additional Information
    st.header("Additional Information")
    st.write(f"**Location:** {st.session_state.latitude:.6f}, {st.session_state.longitude:.6f}")
    st.write(f"**Sunrise:** {st.session_state.solunar_data['sunrise'].strftime('%I:%M %p')}")
    st.write(f"**Sunset:** {st.session_state.solunar_data['sunset'].strftime('%I:%M %p')}")
    st.write(f"**Moon Phase:** {st.session_state.solunar_data['moon_phase']}")

    # Display Map
    st.header("Map")
    m = folium.Map(location=[st.session_state.latitude, st.session_state.longitude], zoom_start=12)
    folium.Marker([st.session_state.latitude, st.session_state.longitude], tooltip="Your Location").add_to(m)
    st_folium(m, width=700, height=500)
else:
    st.info("Please enter parameters and click 'Get Fishing Times'")
