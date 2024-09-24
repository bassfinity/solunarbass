import streamlit as st
from datetime import date, datetime
from streamlit_js_eval import streamlit_js_eval  # Import the function
from src.data_acquisition import get_solunar_data
from src.data_processing import process_solunar_data
from src.solunar_calculations import calculate_major_minor_times
from src.recommendation_engine import generate_recommendations

st.title("🎣 SolunarBass")
st.subheader("Optimal Bass Fishing Times Based on Solunar Theory")

# User Inputs
st.sidebar.header("Input Parameters")

# Add a checkbox to use current location
use_current_location = st.sidebar.checkbox("Use my current location")

if use_current_location:
    # Get the user's location using JavaScript
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
        latitude = loc["latitude"]
        longitude = loc["longitude"]
        st.sidebar.success(f"Location acquired: ({latitude}, {longitude})")
    else:
        st.sidebar.error("Unable to retrieve location. Please allow location access.")
        st.stop()
else:
    # Manual input
    latitude = st.sidebar.number_input("Latitude", value=38.8951, format="%.6f")
    longitude = st.sidebar.number_input("Longitude", value=-77.0364, format="%.6f")

selected_date = st.sidebar.date_input("Date", value=date.today())

if st.sidebar.button("Get Fishing Times"):
    with st.spinner('Fetching data...'):
        raw_data = get_solunar_data(latitude, longitude, selected_date)
        date_str = selected_date.strftime('%Y-%m-%d')  # Convert date to string
        solunar_data = process_solunar_data(raw_data, date_str)
        major_times, minor_times = calculate_major_minor_times(solunar_data)
        recommendations = generate_recommendations(major_times, minor_times)

    st.success("Recommendations Generated!")

    # Display Recommendations
    st.header("Recommended Fishing Times")
    for rec in recommendations:
        start_time = rec['start'].strftime('%I:%M %p')
        end_time = rec['end'].strftime('%I:%M %p')
        st.write(f"**{rec['type']} Period:** {start_time} - {end_time}")

    # Display Additional Information
    st.header("Additional Information")
    st.write(f"**Location:** {latitude:.6f}, {longitude:.6f}")
    st.write(f"**Sunrise:** {solunar_data['sunrise'].strftime('%I:%M %p')}")
    st.write(f"**Sunset:** {solunar_data['sunset'].strftime('%I:%M %p')}")
    st.write(f"**Moon Phase:** {solunar_data['moon_phase']}")
else:
    st.info("Please enter parameters and click 'Get Fishing Times'")
