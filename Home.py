import streamlit as st
from PIL import Image

st.set_page_config(page_title="Portfolio", layout="wide", page_icon=":computer:")

if "page_to_go" not in st.session_state:
    st.session_state.page_to_go = None


# quick links
cols = st.columns(4)

def go(page_name):
    st.session_state.page_to_go = page_name  # set the page to go

cols[0].button("About",  on_click=lambda: go("about_Me"))
cols[1].button("Projects", on_click=lambda: go("projects"))
cols[2].button("Dev Process", on_click=lambda: go("development"))
cols[3].button("Contact", on_click=lambda: go("contact"))

# Perform actual page switch if flag is set
if st.session_state.page_to_go:
    page_file = f"pages/{st.session_state.page_to_go}.py"
    st.session_state.page_to_go = None
    st.switch_page(page_file)

st.markdown("---")

# header
col1, col2 = st.columns([1,3])
with col1:
    try:
        img = Image.open("assets/images/portrait.jpg")
        st.image(img, width=160, caption="Juan Carlos R. Macatangga")
    except:
        st.image("https://placehold.co/160x160?text=Portrait", width=160)

with col2:
    st.title("Juan Carlos R. Macatangga")
    st.markdown("**Data Scientist • ML & Systems Developer**")
    st.markdown("""
    I build data-driven systems, predictive models, and interactive dashboards.
    Explore projects, interactive demos, and deployment-ready artifacts.
    """)

