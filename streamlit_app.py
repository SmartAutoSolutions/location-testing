import streamlit as st
from streamlit_js_eval import get_geolocation
import pandas as pd
from geopy.geocoders import Nominatim

st.title("Secure Login")

# This will prompt the user to "Allow" location access in their browser
location = get_geolocation()

if st.button("Login"):
    if location:
        curr_lat = location['coords']['latitude']
        curr_lon = location['coords']['longitude']
        # Create a simple DataFrame for Streamlit's map
        map_data = pd.DataFrame({'lat': [curr_lat], 'lon': [curr_lon]})
        
        # Display the map
        st.map(map_data)
        geolocator = Nominatim(user_agent="my_streamlit_app")
        location_info = geolocator.reverse(f"{curr_lat}, {curr_lon}")
        st.write(f"Address: {location_info.address}")
        st.success(f"Login successful!")
        st.write(f"Your location is captured: {curr_lat}, {curr_lon}")
        
        # Here you would save curr_lat and curr_lon to your database
    else:
        st.warning("Please allow location access to log in.")
