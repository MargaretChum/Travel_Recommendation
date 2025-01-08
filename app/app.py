import streamlit as st
import sys
sys.path.append('C:/Users/marga/Documents/Personal Project/Travel Recommendation')
from src.travel_log import create_travel_log
from src.recommendation_system import recommend

# Display Travel Log
st.title("Travel Log")
st.write(create_travel_log())

# User Input for Recommendations
activity = st.text_input("Enter activity you enjoyed:", "")
environment = st.text_input("Enter environment you enjoyed:", "")

if activity and environment:
    recommendations = recommend(activity, environment)
    st.write("Based on your preferences, we recommend:")
    st.write(recommendations)
