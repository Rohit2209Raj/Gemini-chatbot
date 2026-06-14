import streamlit as st
import requests

st.set_page_config(
    page_title="Gemini Chat",
    page_icon="🤖"
)

st.markdown(
    "<h1 style='text-align:center';> Gemini Chat </h1>",
    unsafe_allow_html=True
)

question=st.text_area("Enter your thoughts ",height=100)

if st.button("Answer"):
    with st.spinner("Giving you the suitable answer"):
        response=requests.post(
            url='http://127.0.0.1:8000/chat',
            params={'question':question}
        )
        st.success(response)


