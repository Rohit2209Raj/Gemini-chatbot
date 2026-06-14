from main import app 
import streamlit as st
import requests

st.set_page_config(
    page_title="Gemini Chat",
    page_icon="📄",
    layout="centered"
)

st.title("Gemini Chat")
st.text("Explore our Chatbot")


user_api_key = st.text_input('Enter your API_KEY')

user_question = st.text_area("Enter your thoughts",height=200)


if st.button("Answer"):
    if not user_api_key:
        st.error("Enter the API_KEY")
    if not user_question:
        st.error("Enter something to procees")
    else:
        with st.spinner("Answering"):
            response=requests.post(
                "http://127.0.0.1:8000/chat",
                params={
                    "api_key": user_api_key,
                    "question": user_question
                }
            )

            result=response.json()

            st.success(result)
        

