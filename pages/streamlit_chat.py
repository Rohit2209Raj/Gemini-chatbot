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

context=""
if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt := st.chat_input("Enter your thoughts"):

    st.session_state.messages.append({'role':'user','content':prompt})
    with st.chat_message('user'):
        context+=prompt
        st.markdown(context)
    
    response=requests.post(
        url='http://127.0.0.1:8000/chat',
        params={'question':context}
    )

    reply=response.json()

    st.session_state.messages.append({'role':'assistant','content':reply})
    with st.chat_message('assistant'):
        st.markdown(reply)

    


# question=st.text_area("Enter your thoughts ",height=100)

# if st.button("Answer"):
#     with st.spinner("Giving you the suitable answer"):
#         response=requests.post(
#                 url='http://127.0.0.1:8000/chat',
#                 params={'question':question}
#         )

#         # st.success(response.status_code)
#         st.success(response.json())  # See what actually came back

