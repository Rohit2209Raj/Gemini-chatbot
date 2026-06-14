import streamlit as st
from chat import chatting


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
        # if not user_api_key:
        #     st.error("Enter the user_api_key")
        # else:
        #     if check_api_key(user_api_key):
        #         st.success("Redirecting to Gemini Chat")
        #         st.switch_page("pages/login.py")
        #     else:
        #         st.error("invalid user_api_key")

        response = chatting(question)

        st.text(response)


