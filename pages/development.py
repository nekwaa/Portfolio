import streamlit as st

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

st.title("Development Process Summary")

st.markdown("For each project I provide: methodology used, tools, and personal contributions.")

st.subheader("Typical Methodology")
st.write("""
- **Agile / Iterative** for student projects and startup prototypes: short sprints, regular demos, feedback-driven iteration.
- **Waterfall-like** (requirements → design → implementation → test) for small class projects with fixed scope.
""")

st.subheader("Common Tools Used")
st.write("Python, Streamlit, Jupyter, VSCode, Git, Firebase, Power BI, Flutter (for mobile prototypes), Arduino/ESP32 for IoT.")

st.subheader("Role & Contributions")
st.write("""
- Led ML modelling and data pipeline.
- Implemented frontend dashboards and visualization.
- Integrated IoT sensor stream and backend services.
- Created deployment pipelines and documentation.
""")