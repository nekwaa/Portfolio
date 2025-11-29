import streamlit as st
from PIL import Image
import joblib, os

st.set_page_config(page_title="Portfolio", layout="wide", page_icon=":computer:")

if "page_to_go" not in st.session_state:
    st.session_state.page_to_go = None

# quick links
cols = st.columns(4)

def go(page_name):
    st.session_state.page_to_go = page_name  # set the page to go

cols[0].button("Home",  on_click=lambda: go("Home"))
cols[1].button("Projects", on_click=lambda: go("pages/projects"))
cols[2].button("Dev Process", on_click=lambda: go("pages/development"))
cols[3].button("Contact", on_click=lambda: go("pages/contact"))

# Perform actual page switch if flag is set
if st.session_state.page_to_go:
    page_file = f"{st.session_state.page_to_go}.py"
    st.session_state.page_to_go = None
    st.switch_page(page_file)

st.markdown("---")

st.session_state.page = "Projects"


page = st.query_params.get("page", None)
if page:
    st.session_state.page = page

st.title("Projects")
st.write("Here are the systems and applications I have developed:")


st.title("Project Showcase")

# Project: IoT Indoor Air Quality
with st.expander("📌 IoT Indoor Air Quality & Noise Monitoring System", expanded=True):
    st.write("**Overview:** Real-time IoT system that monitors indoor air quality (CO2, PM2.5, humidity) and noise levels with predictive models for short-term forecasting.")
    st.write("**Problem:** Indoor health and productivity are affected by hidden air-quality issues. This system gives actionable insights and alerts.")
    st.write("**Features:** Realtime dashboard, predictive model, alerts, data logging.")
    col1, col2 = st.columns([1,1])
    with col1:
        if os.path.exists("assets/images/iaq_dashboard.png"):
            st.image("assets/images/iaq_dashboard.png", caption="Dashboard example", use_column_width=True)
        else:
            st.write("https://airqualitypredictionsystem.streamlit.app​")

    st.markdown("**System architecture:** Sensors → Microcontroller (ESP32) → MQTT → Backend API → DB → Streamlit Dashboard + ML Model (prediction).")
    
    # Interactive ML demo (synthetic example)
    st.markdown("### Live ML demo (synthetic)")
    n = st.slider("Number of recent samples to predict", 5, 60, 15)
    import pandas as pd, numpy as np
    rng = np.random.RandomState(0)
    samples = pd.DataFrame({
        "CO2": np.clip(400 + np.cumsum(rng.randn(n))*3, 380, 950),
        "PM2.5": np.clip(5 + np.abs(rng.randn(n))*4, 0, 200),
        "noise_db": np.clip(40 + rng.randn(n)*3, 30, 90)
    })
    st.write(samples.tail(5))
    if st.button("Run synthetic forecast"):
        # small synthetic prediction (moving average)
        pred = samples["CO2"].rolling(3).mean().iloc[-1] + np.random.randn()*2
        st.success(f"Predicted next CO2 (ppm): {pred:.1f} — demo result")
