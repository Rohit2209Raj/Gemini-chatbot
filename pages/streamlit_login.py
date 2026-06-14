import streamlit as st
from verify import check_api_key


st.set_page_config(
    page_title="login",
    page_icon="🤖"
)

st.markdown(
    "<h1 style='text-align:center';> Login to access Gemini Chat </h1>",
    unsafe_allow_html=True
)

user_api_key=st.text_input("Enter your user_api_key")

if st.button("Login"):
    with st.spinner("Verifying"):
        if not user_api_key:
            st.error("Enter the user_api_key")
        else:
            if check_api_key(user_api_key):
                st.success("Redirecting to Gemini Chat")
                st.switch_page("pages/streamlit_chat.py")
            else:
                st.error("invalid user_api_key")

