# India_AQI_Checking_App
This App Helps to check  Air Quality Index of your Area in India based on Pincode input
# 🌿 India AQI Expert Dashboard

An AI-powered environmental dashboard that provides Air Quality Index (AQI) insights for any Indian location using its **PINCODE**. The app combines real-world geocoding with Google's Gemini AI to offer health recommendations and local environmental analysis.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)

## 🚀 Features
- **Pincode Search:** Enter any 6-digit Indian PINCODE to locate an area.
- **Interactive Map:** Visualizes the location instantly using OpenStreetMap.
- **AI Analysis:** Uses Google Gemini (via LangChain) to generate:
    - Expected AQI categories.
    - Tailored health advice for children and the elderly.
    - Regional pollution factor analysis.
- **Custom Eco-Theme:** A polished green and blue environmental dashboard UI.
- **Downloadable Reports:** Save the AI's analysis as a `.txt` file with one click.

## 🛠️ Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io/)
- **LLM Orchestration:** [LangChain](https://python.langchain.com/)
- **AI Model:** Google Gemini 1.5 Flash
- **Geocoding:** [GeoPy](https://geopy.readthedocs.io/) (Nominatim API)
- **Data Handling:** Pandas

## 📋 Prerequisites
Before running this project, you will need:
- Python 3.8 or higher.
- A Google Gemini API Key (Get it from [Google AI Studio](https://aistudio.google.com/)).

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sanjayforgenai-dev/India_AQI_Checking_App/blob/main.git](https://github.com/your-username/india-aqi-dashboard.git)
   cd india-aqi-dashboard
