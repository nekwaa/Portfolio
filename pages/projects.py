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

with st.expander("Project SBAFN — Street-based Assessment for Flood-prone Neighborhoods"):
    st.subheader("Overview")
    st.write("""
    Project SBAFN is an AI-powered system that assesses flood-proneness of streets in Metro Manila at a **street-segment level**.  
    Unlike traditional area-based hazard maps, this project provides **granular, actionable insights** for local governments, urban planners, and commuters.
    """)
    st.subheader("Problem")
    st.write("""
    Flooding in Metro Manila remains a persistent challenge due to rapid urbanization, inadequate drainage, and extreme rainfall.  
    Current hazard maps operate at neighborhood or barangay level, leaving critical **street-level gaps** in actionable information for planning and mobility.
    """)
    st.subheader("Methodology")
    st.write("""
    The project follows a multi-phase methodology:

    1. **Data Acquisition:** Street-level images, DEM, road networks, rainfall data, and flood incidents.  
    2. **Feature Engineering:** Extract physical, hydrologic, and streetscape features.  
    3. **Model Development:** Train AI models to predict flood-proneness; ensure explainability.  
    4. **Application Development:** Interactive web app showing flood-proneness scores per street.  
    5. **Evaluation:** Validate predictions against historical flood records and benchmark with Project NOAH.
    """)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("assets/images/10.jpg",  width=650)
    with col2:
        st.image("assets/images/12.jpg",  width=650)

with st.expander("MSME Lending & Blockchain Solution"):
    st.subheader("Overview")
    st.write("""
    This project provides a **data-driven, equitable lending system** for MSMEs in the Philippines, 
    especially in underserved sectors like agriculture, fisheries, and indigenous communities.  
    By leveraging **machine learning** and optionally **blockchain**, the solution improves credit accessibility 
    and transparency for banks and borrowers.
    """)

    st.subheader("Problem Statement")
    st.write("""
    Many MSMEs struggle to access loans due to lack of formal financial records.  
    Traditional lending practices often exclude businesses from indigenous, agricultural, and fisheries sectors.  
    This solution aims to **reduce financial exclusion** and support business growth.
    """)

    st.subheader("Solution Approach")
    st.write("""
    **Part I - Machine Learning for Alternative Credit Assessment**  
    Uses non-financial metrics such as social impact, environmental affiliation, number of guarantors, seasonal trends, geolocation, and utility bill payments to evaluate loan eligibility.

    **Part II - Blockchain Integration (Optional)**  
    Provides a decentralized, tamper-proof ledger for transaction monitoring, improving transparency and trust in loan evaluations.  
    Supports smart contracts for validation and risk assessment via ML models.

    **Part III - Loan Settings Restructuring**  
    Proposes longer repayment periods and adjusted interest rates to accommodate MSMEs' financial capabilities.
    """)

    st.subheader("Technical Details & Technology Stack")
    st.write("""
    **Machine Learning:** scikit-learn, pandas, NumPy, Jupyter Notebook  
    **Blockchain:** Hyperledger Fabric, PoA/Raft consensus, Chaincode (Node.js)  
    **Data Storage:** CouchDB, LevelDB  
    **Integration:** FabricSDK, REST APIs  
    **Deployment:** Docker, AWS/Azure/GCP  
    """)

    col1, col2, col3 = st.columns([1, 2, 1])  # middle column is wider
    with col2:
        st.image("assets/images/banner.png",  width=650)

with st.expander("IoT Indoor Air Quality & Noise Monitoring System"):
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