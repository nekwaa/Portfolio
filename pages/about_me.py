import streamlit as st
from PIL import Image

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

st.title("About Me")

col1, col2 = st.columns([1,2])

with col1:
    try:
        img = Image.open("assets/images/portrait.jpg")
        st.image(img, width=220)
    except:
        st.image("https://placehold.co/220x220?text=Portrait")

with col2:
    st.markdown("""
**Juan Carlos R. Macatangga**  
Data Scientist & Computer Science graduate.

I am a motivated Computer Science graduate with hands-on experience in Python, C++, and Power BI. Passionate about leveraging data and technology to solve real-world problems and build production-ready systems.  
""")

st.subheader("Skills")
cols = st.columns(2)
cols[0].markdown("**Technical**\n- Python\n- C++\n- Java\n- Pandas, NumPy\n- Matplotlib, Plotly\n- Power BI\n- Jupyter, VSCode")
cols[1].markdown("**Soft Skills**\n- Critical thinking\n- Teamwork\n- Communication\n- Adaptability")

st.subheader("Tools & Technologies")
st.write("VSCode • Jupyter • Git • Power BI • Firebase • Flutter (basic) • Streamlit")

st.markdown("---")
st.subheader("Contact")
st.write("📍 Lucena City")
st.write("📱 09381797461")
st.write("📧 juanmacatangga1@gmail.com")