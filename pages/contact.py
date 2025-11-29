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

st.title("Contact")
st.write("I'd love to hear from you. Reach out via any of the following channels:")

st.markdown("""
- **Email:** juanmacatangga1@gmail.com  
- **Phone:** 09381797461  
- **Location:** Lucena City
""")

st.subheader("Send me a quick message")
name = st.text_input("Your name")
email = st.text_input("Your email")
message = st.text_area("Message")
if st.button("Send"):
    if name and email and message:
        st.success("Message submitted! (This demo doesn't send emails — wire to SMTP or zapier in deployment.)")
    else:
        st.error("Please fill all fields.")