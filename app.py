import streamlit as st
import threading
import uvicorn
from main import app as fastapi_app



# Start FastAPI in background thread
def run_fastapi():
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)

thread = threading.Thread(target=run_fastapi, daemon=True)
thread.start()

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