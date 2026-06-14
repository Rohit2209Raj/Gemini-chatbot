import streamlit as st

st.set_page_config(
    page_title="Gemini Chat",
    page_icon="🤖"
)

st.markdown(
    "<h1 style='text-align:center;'>Gemini Chat</h1>",
    unsafe_allow_html=True
)

st.write("Welcome to the AI Chat Application")

st.info("Login first to access chat")

if st.button("Go to Login"):
    st.switch_page("pages/streamlit_login.py")