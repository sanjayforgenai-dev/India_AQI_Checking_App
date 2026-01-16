from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from geopy.geocoders import Nominatim
import streamlit as st
import pandas as pd
import os

# 1. Setup API Key
os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# Initialize Geocoding
geolocator = Nominatim(user_agent="india_aqi_checker")

# --- CUSTOM CSS FUNCTION ---
def apply_custom_style():
    st.markdown("""
        <style>
        /* Main background and text */
        .stApp {
            background-color: #f0f7f4;
        }
        
        /* Header styling */
        h1 {
            color: #2d5a27; /* Forest Green */
            font-family: 'Helvetica Neue', sans-serif;
        }
        
        /* Input box styling */
        .stTextInput > div > div > input {
            border: 2px solid #3498db; /* Sky Blue */
        }
        
        /* Button styling */
        div.stButton > button:first-child {
            background-color: #2d5a27;
            color: white;
            border-radius: 10px;
            border: none;
            width: 100%;
            height: 3em;
        }
        
        div.stButton > button:hover {
            background-color: #3498db;
            color: white;
        }

        /* Success message styling */
        .stAlert {
            background-color: #e8f4fd;
            border-left: 5px solid #3498db;
        }
        </style>
    """, unsafe_allow_html=True)

# --- Streamlit UI ---
st.set_page_config(page_title="Eco-Dashboard AQI", page_icon="🌿", layout="wide")

# Apply the theme
apply_custom_style()

# Sidebar for Theme Toggle / Info
with st.sidebar:
    st.title("Settings")
    theme_choice = st.radio("Choose Dashboard Mode", ("Environmental (Default)", "High Contrast"))
    st.info("This app uses AI to provide environmental insights based on regional data.")

st.header("🌿 PINCODE Based Air Quality Index Report Generator App")
st.markdown("---")

# Layout columns
col1, col2 = st.columns([1, 1])

with col1:
    pincode = st.text_input("Enter 6-digit Indian PINCODE", placeholder="e.g. 110001")
    find_button = st.button("Find AQI")

# Logic
if find_button:
    if len(pincode) == 6 and pincode.isdigit():
        location = geolocator.geocode(f"{pincode}, India")
        
        if location:
            with col2:
                st.subheader("📍 Location Map")
                map_data = pd.DataFrame({'lat': [location.latitude], 'lon': [location.longitude]})
                st.map(map_data, zoom=12)
            
            with col1:
                st.success(f"location: {location.address}")
                
                # AI Analysis
                gemini_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
                aqi_template = "As an expert, analyze the typical AQI for PINCODE {pincode} in {location}."
                aqi_prompt = PromptTemplate(template=aqi_template, input_variables=['pincode', 'location'])
                aqi_chain = aqi_prompt | gemini_model
                
                response = aqi_chain.invoke({"pincode": pincode, "location": location.address})
                
                st.markdown("### 📊 AI Analysis")
                st.info(response.content)
                
                st.download_button(
                    label="📥 Download Report",
                    data=response.content,
                    file_name=f"AQI_{pincode}.txt"
                )
        else:
            st.error("PINCODE not found.")
    else:
        st.warning("Invalid PINCODE.")
