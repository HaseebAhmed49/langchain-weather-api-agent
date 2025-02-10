import streamlit as st
import requests

st.set_page_config(page_title="AI Weather App", page_icon="🌦", layout="centered")
st.title("🌍 AI-Powered Weather App")

# User Input
city = st.text_input("Enter city name:", "London")

if st.button("Get Weather"):
    with st.spinner("Fetching weather data using AI agent..."):
        api_url = f"http://127.0.0.1:8000/weather/{city}"  # Ensure FastAPI backend is running
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            if "response" in data:
                st.subheader(f"Weather Info for {data['city']}:")
                st.write(data["response"])  # LangChain agent response
            else:
                st.error("Unexpected response format from the API.")
        else:
            st.error("Failed to fetch weather data. Please try again.")